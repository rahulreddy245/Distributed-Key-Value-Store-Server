-------------------------------------------------
README : Consistent Key-Value Store
-------------------------------------------------

------------
INTRODUCTION
------------
We have developed our code in Python 2.7 and used Thrift-0.9.3 library. This program is developed on windows 10.
The program has the following 
	1.kvserver.py          --> a key value server 
	2.kvsequencer.py       --> a sequence id generator  
	3.kvclient.py          --> a client application
	4.checker.py           --> a consistency checker 
	5.consistency_check.py --> a single application which covers items 2,3 and 4.
	
There are also two thrift libraries kvstore and kvSequencer, generated from the thrift file, used as a communication mechanism between the servers
and the clients.

---------------
PRE-REQUISITES
---------------
Please follow the following steps before running the project.
1. Install Python 2.7 to your PC. 
2. If you don't have Thrift. Download the thrift repository from github. Link- https://github.com/apache/thrift (Not the exe, but the actual repository).
3. While in Terminal, navigate to the directory, /"path to thrift folder"/lib/py/.  You should have setup.py file present in that folder.
4. Use the command python setup.py to install using command line. (This should install the thrift python libraries)
5. In Terminal type 'pip install networkx' to install NetworkX, an external python library used in our code.
6. Now navigate to the project folder /"path to project folder"/gen-py/.


------------------------------
EXECUTING OUR CODE FOR TESTING
------------------------------
Please follow the steps in prerequisites section before executing this code.
1. After you unzip the project folder we sent you and navigate to path in command line: /"path to project folder"/gen-py/.
2. Step 1: Run Server: A kvserver should be run.  hostname:port details should be saved.
3. Step 2: Run clients consistency_check application: Open another terminal and execute below command:
	"python ./consistency_check.py -server hostname:port"
	a.This will spawn a sequence server. This will give seqence numbers to the client transcations.
	b.Starts the kvclient application. It will create a log file which shows the servers replies. Client will start multiple threads and stop 
	automatically. While running it randomly performs set,get from kvstore via kvserver and kvsequenceserver.
    c.Finally runs the checker application which will check the consistency of the server based on the logs captured.	
	
	Exit code:
	If there is no issues. we do nothing and the program will exit with exit code 0 by default.
	If there is an issue we are using exit(1), so the program will exit with exit code 1.
4. Please check the screenshots, if you need more please contact anyone of us.

----------------------------
EXECUTING OUR CODE SANDALONE
----------------------------
Please follow the steps in prerequisites section before executing this code.
1. After you unzip the project folder we sent you and navigate to path in command line: /"path to project folder"/gen-py/.
2. Step 1: Run Server: On terminal type "python kvserver.py". This should print the hostname to the terminal.
3. Step 2: Run Sequencer: Open another terminal type "python kvsequenceserver.py". This should print the hostname to the terminal.
4. Step 3: Run Client: Open another terminal and execute below command:
	"python./kvclient.py -server localhost:9090"
5. Client will start multiple threads and stop automatically. While running it randomly performs set,get from kvstore via kvserver and kvsequenceserver.
6. Step 4: Run Checker: Once client stops, open another terminal and type "python checker.py".
7. Please check the screenshots, if you need more please contact anyone of us.


---------------------
SCREENSHOTS AND CODE
---------------------
Screenshots of the running program can be found in the Screenshots folder. All our code and other files will be in the gen-py folder.

---------------
GROUP MEMBERS
---------------
Group # 4
Rahul Reddy (rra304@nyu.edu)
Suraj Patel (skp392@nyu.edu)
Jubin Soni (jas1464@nyu.edu)
Balaji Reddy (bbr234@nyu.edu)
