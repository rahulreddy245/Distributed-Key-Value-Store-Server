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
import socket, kvSequencer
from kvSequencer import SequenceService
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
host = socket.gethostname()

class KVSequenceClient():
    def __init__(self, kvcConnectingHost):
        # Make Socket
        kvcServerAddr, kvcServerPort = kvcConnectingHost.split(":")
        self.transport = TSocket.TSocket(kvcServerAddr, int(kvcServerPort))

        # Buffering
        self.transport = TTransport.TBufferedTransport(self.transport)

        # Wrap in protocol
        protocol = TBinaryProtocol.TBinaryProtocol(self.transport)

        # Create client
        self.client = SequenceService.Client(protocol)

        # Connect!
        self.transport.open()
        print "Connected to server: {0}".format(str(kvcConnectingHost))

    def get(self):
        result = 0
        #print("inside get")
        result = self.client.getnextsequenceid()
        print("got the sequence id :%d" %(result))
        return result


def usage():
    print ("Correct usage: kvsequenceclient -server host:port")

def main(argv):
    # parsing command line arguments
    err=2
    if argv[0] != "-server":
        usage()
        sys.exit(err)

    kvcConnectingHost = argv[1]
    kvc = KVSequenceClient(kvcConnectingHost)

    kvc.get()

if __name__ == "__main__":
    try:
        main(sys.argv[1:])
    except Exception as e:
        sys.stderr.write("Error: "+str(e))
        sys.exit(2)
