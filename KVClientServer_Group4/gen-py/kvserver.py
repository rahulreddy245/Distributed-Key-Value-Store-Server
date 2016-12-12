'''
Group Number: 4

#kvserver.py;

TeamMembers:
Rahul Reddy (rra304)
Suraj Patel (skp392)
Jubin Soni  (jas1464)
Balaji Reddy(bbr234)
'''

import sys
sys.path.append('gen-py')
import socket
import threading
from kvstore import KVStore
from kvstore.ttypes import ErrorCode, Result
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
host = socket.gethostname()


class kvserver:
    kv_dict = {}
    lock = threading.Lock()
    def kvset(self, key, value):
        with self.lock:
            self.kv_dict[key] = value
            try:
                print ("Entry added - Key: {0}, Value: {1}".format(key, value))
            except Exception as e:
                return Result(None, ErrorCode.kError, e.message)
            return Result(None, ErrorCode.kSuccess, None)

    def kvget(self, key):
        with self.lock:
            try:
                value = self.kv_dict[key]
            except KeyError:
                return Result(None, ErrorCode.kKeyNotFound, "Key: "+key+", Not present in store")
            except Exception as e:
                return Result(None, ErrorCode.kError, e.message)
            return Result(value, ErrorCode.kSuccess, None)

    def kvdelete(self, key):
        try:
            value = self.kv_dict[key]
            del self.kv_dict[key]
        except KeyError:
            return Result(None, ErrorCode.kKeyNotFound, "Key: "+key+", Not present in store")
        except Exception as e:
            return Result(None, ErrorCode.kError, e.message)
        print ("Entry Deleted - Key: {0}".format(key))
        return Result(value, ErrorCode.kSuccess, None)

if __name__ == "__main__":
    try:
        handler = kvserver()
        processor = KVStore.Processor(handler)
        transport = TSocket.TServerSocket(port=9090)
        tfactory = TTransport.TBufferedTransportFactory()
        pfactory = TBinaryProtocol.TBinaryProtocolFactory()
        server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)
        print("Starting Server: %s"%host)
        server.serve()
        print("Done.")

    except Exception as err:
        print("Error: %s" %str(err))
