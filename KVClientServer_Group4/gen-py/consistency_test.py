#!/usr/bin/python

import sys
import kvclient
import kvsequenceserver
import checker
import threading

def usage():
    print ("Correct usage: kvclient -server host:port")

def main(argv):

    # parsing command line arguments
    err = 2
    if argv[0] != "-server":
        usage()
        sys.exit(err)
    if argv.__len__() != 2:
        usage()
        sys.exit(err)
    #print("starting sequence server\n")
    #seqthread =  threading.Thread(target=kvsequenceserver.main())
    #seqthread.start()

    #print("starting Client\n")
    #clientthread = threading.Thread(kvclient.main(argv))
    #clientthread.start()
    kvclient.main(argv)

    #checker.main()
    #print("starting checker\n")
    #checkerthread = threading.Thread(checker.main())
    #checkerthread.start()




if __name__ == "__main__":
    try:
        main(sys.argv[1:])
    except Exception as e:
        sys.stderr.write("Error: "+str(e))
        sys.exit(2)