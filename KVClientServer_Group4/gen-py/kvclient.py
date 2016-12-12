#!/usr/bin/python
'''
Group Number: 4

#kvclient.py;

TeamMembers:
Rahul Reddy (rra304)
Suraj Patel (skp392)
Jubin Soni  (jas1464)
Balaji Reddy(bbr234)
'''

import sys
import subprocess
sys.path.append('gen-py')
import socket, kvserver, kvSequencer
from kvSequencer import SequenceService
from kvstore import KVStore
from kvstore.ttypes import ErrorCode
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
import multiprocessing
import threading, sys, os
import time
import random
from kvsequenceclient import KVSequenceClient

host = socket.gethostname()

class kvclient():
    def __init__(self, kvcConnectingHost):
        #Sequence variable to used for value
        self.seqstart = 0
        self.seqend = 0
        self.seq = 0

        #Key value on which the project is run
        self.key = 'DS:'

        #lock so that the sequence is incremented and assigned atomically
        self.lock = threading.Lock()

        #Connect to the Key Value Store at the address mentioned in the command prompt
        # Make Socket
        kvcServerAddr, kvcServerPort = kvcConnectingHost.split(":")
        self.transport = TSocket.TSocket(kvcServerAddr, int(kvcServerPort))

        # Buffering
        self.transport = TTransport.TBufferedTransport(self.transport)

        # Wrap in protocol
        protocol = TBinaryProtocol.TBinaryProtocol(self.transport)

        # Create client
        self.client = KVStore.Client(protocol)

        # Connect!
        self.transport.open()
        print "Connected to server: {0}".format(str(kvcConnectingHost))

        self.sequenceClient = KVSequenceClient('localhost:10100')

    def set(self, key, value):
        try:
            setResult = self.client.kvset(key, value)
            if setResult.error == ErrorCode.kSuccess:
                print ("Key: %s Value: %s, successfully stored" % (key, value))
                #sys.exit(setResult.error) #exitCode
            else:
                sys.stderr.write("Set Error: "+setResult.errortext) #errorText
                #sys.exit(setResult.error)#exitCode
        except ErrorCode as errortext:
            sys.stderr.write("Set Error: "+str(errortext)) #errorText
            #sys.exit(setResult.error)#exitCode

    def get(self, key):
        try:
            getResult = self.client.kvget(key)
            if getResult.error == ErrorCode.kSuccess:
                print ("Key: {1} Value: {0}, successfully retrieved".format(getResult.value, key))
                return getResult.value
                #sys.exit(getResult.error)
            else:
                sys.stderr.write("Get Error: "+str(getResult.errortext)) #errorText
                #sys.exit(getResult.error) #exitCode
        except ErrorCode as errortext:
            sys.stderr.write("Set Error: "+str(errortext)) #errorText
            #sys.exit(getResult.error) #exitCode

    def delete(self, key):
        try:
            delResult = self.client.kvdelete(key)
            if delResult.error == ErrorCode.kSuccess:
                print ("Key: %s, successfully deleted" % key)
                #sys.exit(delResult.error) #erroText
            else:
                sys.stderr.write("Delete Error: "+delResult.errortext) #errorText
                #sys.exit(delResult.error) #exitCode
        except ErrorCode as errortext:
            sys.stderr.write("Set Error: "+str(errortext)) #errorText
            #sys.exit(delResult.error) #exitCode

    def worker(self):
        # print ("inside worker")
        while (1):
            self.seqstart = self.sequenceClient.get()

            #print ("inside while worker:%d"% (seqstart))
            opcode = random.randint(0, 1)
            if (opcode == 0):
                self.seq = str(self.seqstart + 1)
                # with self.lock:
                self.set(self.key, self.seq)
            else:
                self.seq = self.get(self.key)
            self.seqend = self.sequenceClient.get()
            #print ("inside while worker:%d" %(seqend))

            self.lock.acquire(True)
            f = open("log.txt", 'a')

            # Writing sequence start and end numbers, opcode and value set/retrieved. Could change opcode with string "S" and "G" if needed.
            #if (self.seq != None):
            f.write(str(self.seqstart) + "," + str(opcode) + "," + str(self.seq) + "," + str(self.seqend) + "\n")
            f.close()
            self.lock.release()

    def __del__(self):
        self.transport.close()

def usage():
    print ("Correct usage: kvclient -server host:port -<remote method> ")



def killer():
    """Killer thread"""
    time.sleep(20)
    os._exit(1)

def main(argv):
    #delete log.txt if present
    if(os.path.isfile("log.txt")):
        os.remove("log.txt")

    # parsing command line arguments
    err=2
    if argv[0] != "-server":
        usage()
        sys.exit(err)
    if argv.__len__()!=2:
        usage()
        sys.exit(err)

    kvcConnectingHost = argv[1]
    numClients = 12

    kvclientarray = []
    for i in range(numClients):
        kvc = kvclient(kvcConnectingHost)
        kvc.set(kvc.key,'0')
        kvclientarray.append(kvc)

    k = threading.Thread(target=killer)
    k.start()

    threads = []
    for i in range(numClients):
       t = threading.Thread(target=kvclientarray[i].worker)
       threads.append(t)
       t.start()
    """
    threads = []
    for i in range(5):
       t = threading.Thread(target= worker,args=(kvc,))
       threads.append(t)
       t.start()
    """


if __name__ == "__main__":
    try:
        main(sys.argv[1:])
    except Exception as e:
        sys.stderr.write("Error: "+str(e))
        sys.exit(2)
