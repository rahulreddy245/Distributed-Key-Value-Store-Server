#!/usr/bin/python

import sys
import kvclient
import subprocess
import threading
import time

def usage():
    print ("Correct usage: kvclient -server host:port")

def main(argv):
    start = time.time()
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
    pro = subprocess.Popen([sys.executable, 'kvsequenceserver.py'], creationflags=subprocess.CREATE_NEW_CONSOLE)

    print("starting Client\n")
    clientthread = threading.Thread(kvclient.main(argv))
    clientthread.start()

    #os.kill(pro.pid, signal.CTRL_BREAK_EVENT)
    subprocess.call(['taskkill', '/F', '/T', '/PID', str(pro.pid)])

    import checker

    #checker.main()
    print("starting checker\n")
    checkerthread = threading.Thread(checker.main())
    checkerthread.start()
    print(stop - start)


if __name__ == "__main__":
    try:
        main(sys.argv[1:])
    except Exception as e:
        sys.stderr.write("Error: "+str(e))
        sys.exit(2)