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
import socket
from kvstore import KVStore
from kvstore.ttypes import ErrorCode
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
import threading
import os
import random
import itertools
from kvsequenceclient import KVSequenceClient

sys.path.append('gen-py')
host = socket.gethostname()
threadlock = threading.Lock()
cont = itertools.count()


class kvclient():
    def __init__(self, kvcconnectinghost):
        # Sequence variable to used for value
        self.seqstart = 0
        self.seqend = 0
        self.seq = 0
        self.seqlimit = 8000
        self.opcode = 2

        # Key value on which the project is run
        self.key = 'DS:'

        # lock so that the sequence is incremented and assigned atomically
        self.lock = threading.Lock()

        # Connect to the Key Value Store at the address mentioned in the command prompt
        # Make Socket
        kvcserveraddr, kvcserverport = kvcconnectinghost.split(":")
        self.transport = TSocket.TSocket(kvcserveraddr, int(kvcserverport))

        # Buffering
        self.transport = TTransport.TBufferedTransport(self.transport)

        # Wrap in protocol
        protocol = TBinaryProtocol.TBinaryProtocol(self.transport)

        # Create client
        self.client = KVStore.Client(protocol)

        # Connect!
        self.transport.open()
        print "Connected to server: {0}".format(str(kvcconnectinghost))

        self.sequenceClient = KVSequenceClient('localhost:10100')

    def set(self, key, value):
        try:
            setresult = self.client.kvset(key, value)
            if setresult.error == ErrorCode.kSuccess:
                print ("Key: %s Value: %s, successfully stored\n" % (key, value))
                # sys.exit(setResult.error) #exitCode
            else:
                sys.stderr.write("Set Error: "+setresult.errortext)
                # sys.exit(setResult.error)#exitCode
        except ErrorCode as errortext:
            sys.stderr.write("Set Error: "+str(errortext))
            # sys.exit(setResult.error)#exitCode

    def get(self, key):
        try:
            getresult = self.client.kvget(key)
            if getresult.error == ErrorCode.kSuccess:
                print ("Key: {1} Value: {0}, successfully retrieved\n".format(getresult.value, key))
                return getresult.value
                # sys.exit(getResult.error)
            else:
                sys.stderr.write("Get Error: "+str(getresult.errortext))
                # sys.exit(getResult.error) #exitCode
        except ErrorCode as errortext:
            sys.stderr.write("Set Error: "+str(errortext))
            # sys.exit(getResult.error)

    def delete(self, key):
        try:
            delresult = self.client.kvdelete(key)
            if delresult.error == ErrorCode.kSuccess:
                print ("Key: %s, successfully deleted" % key)
                # sys.exit(delResult.error) #erroText
            else:
                sys.stderr.write("Delete Error: "+delresult.errortext)
                # sys.exit(delResult.error) #exitCode
        except ErrorCode as errortext:
            sys.stderr.write("Set Error: "+str(errortext))
            # sys.exit(delResult.error) #exitCode

    def worker(self):
        # print ("inside worker")
        while 1:
            self.seqstart = self.sequenceClient.get()

            # print ("inside while worker:%d"% (seqstart))
            self.opcode = random.randint(0, 1)
            if self.opcode == 0:
                self.seq = str( cont.next())
                # with self.lock:
                self.set(self.key, self.seq)
            elif self.opcode ==1:
                self.seq = self.get(self.key)
            self.seqend = self.sequenceClient.get()
            # print ("inside while worker:%d" %(seqend))

            threadlock.acquire(True)
            with open("log.txt", 'a',0) as f:

                # Writing sequence start and end numbers, opcode and value set/retrieved.
                # Could change opcode with string "S" and "G" if needed.
                # if (self.seq != None):
                f.write(str(self.seqstart) + "," + str(self.opcode) + "," + str(self.seq) + "," + str(self.seqend) + "\n")

            threadlock.release()
            if self.seq > self.seqlimit:
                print("  Exiting Thread.\n")
                break

    def __del__(self):
        self.transport.close()


def usage():
    print ("Correct usage: kvclient -server host:port")


# def killer():
#    """Killer thread"""
#    time.sleep(20)
#    os._exit(1)

def main(argv):
    # delete log.txt if present
    if (os.path.isfile("log.txt")):
        os.remove("log.txt")


    # parsing command line arguments
    err = 2
    if argv[0] != "-server":
        usage()
        sys.exit(err)
    if argv.__len__() != 2:
        usage()
        sys.exit(err)

    kvcconnectinghost = argv[1]
    numclients = 12

    kvclientarray = []
    for i in range(numclients):
        kvc = kvclient(kvcconnectinghost)
        kvc.set(kvc.key, '0')
        kvclientarray.append(kvc)

    # k = threading.Thread(target=killer)
    # k.start()

    threads = []
    for i in range(numclients):
        t = threading.Thread(target=kvclientarray[i].worker)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
    print('Finish.')


if __name__ == "__main__":
    try:
        main(sys.argv[1:])
    except Exception as e:
        sys.stderr.write("Error: "+str(e))
        sys.exit(2)
