-------------------------------------------------
README : Consistent Key-Value Store
-------------------------------------------------
---------------
GROUP MEMBERS
---------------
Group # 4
Rahul Reddy (rra304@nyu.edu)
Suraj Patel (skp392@nyu.edu)
Jubin Soni (jas1464@nyu.edu)
Balaji Reddy (bbr234@nyu.edu)

------------
INTRODUCTION
------------
We have developed our code in Python 2.7 and used Thrift-0.9.3 library. This program is developed on windows 10.
The program has the following 
	1.kvserver.py          --> a key value server 
	2.kvsequencer.py       --> a sequence id generator  
	3.kvclient.py          --> a client application
	4.checker.py           --> a consistency checker 
	5.consistency_check.py --> a single application which covers items 2,3 and 4. [NOTE: had to use windows specific code to create subprocess in python]
	
There are also two thrift libraries kvstore and kvSequencer, generated from the thrift file, used as a communication mechanism between the servers
and the clients.

---------------
PRE-REQUISITES
---------------
Please follow the following steps before running the project.
1. Install Python 2.7 to your PC. We worked on Windows 10 PC for the project.
2. If you don't have Thrift. Download the thrift repository from github. Link- https://github.com/apache/thrift (Not the exe, but the actual repository).
3. While in Terminal, navigate to the directory, /"path to thrift folder"/lib/py/. This is for seting up the python lib for thrift. You should see a setup.py file present in that folder.
4. Use the command "python setup.py" to install using command line. (This should install the thrift python libraries)
5. In Terminal type "pip install networkx" to install NetworkX, an external python library used in our code.
6. Now navigate to the project folder /"path to project folder"/gen-py/.


-----------------------------------------
EXECUTING OUR CODE FOR TESTING on WINDOWS - min config core i3 6gb ram
-----------------------------------------
Please follow the steps in prerequisites section before executing this code.
1. After you unzip the project folder we sent you navigate to project path in command line:  /"path to project folder"/gen-py/.
2. Step 1: Run Server: A kvserver should be run.  "hostname:port" details should be saved.
3. Step 2: Run clients: consistency_check.py application should be executed. Open another terminal and execute the command: "python consistency_check.py -server hostname:port"
	a.This will spawn a sequence server. This will give seqence numbers to the client transcations.
	b.Starts the kvclient application. This will create a log file which shows the key-value store-retrival trace.
	  Clients will start multiple threads and stop automatically. While running they randomly perform set,get from kvserver using kvsequenceserver as logical clock.
    c.Finally once the clients die down after set period of time it runs the consistency checking application which will check the consistency of the server's behaviour
      based on the logs captured.
	
	Exit code:
	If there is no issues. we do nothing and the program will exit with exit code 0 by default.
	If there is an issue we are using exit(1), so the program will exit with exit code 1.
	If there is something abnormal which is out of the running parameters of the program it will exit with exit code 2.

4. Please check the screenshots for reference, if you need more info please contact anyone of us from the group.

-----------------------------------------
EXECUTING OUR CODE FOR TESTING on LINUX - min config core i3 6gb ram
-----------------------------------------
We dont have a LINUX PC so could not edit the project to run as a singele consistency_check.py client application.
Please follow the below instructions if it is a must to run in a LINUX environment.

Please follow the steps in prerequisites section before executing this code.
1. After you unzip the project folder we sent you navigate to project path in command line:  /"path to project folder"/gen-py/.
2. Step 1: Run Server: A kvserver should be run.  "hostname:port" details should be saved.
3. Step 2: Run kvsequenceserver. Open another terminal and execute the command: "python kvsequenceserver.py"
4. Step 3: Run clients: consistency_check.py application should be executed. Open another terminal and execute the command: "python consistency_check.py -server hostname:port"

Make sure you have executable permission for "consistency_test.py" file. To add executable permission on linux, run the command - chmod +x consistency_test.py
Once you execute the above command, run the file using the command - ./consistency_test.py -server "SERVERNAME"

	a.Starts the kvclient application. This will create a log file which shows the key-value store-retrival trace.
	  Clients will start multiple threads and stop automatically. While running they randomly perform set,get from kvserver using kvsequenceserver as logical clock.
    b.Finally once the clients die down after set period of time it runs the consistency checking application which will check the consistency of the server's behaviour
      based on the logs captured.

	Exit code:
	If there is no issues. we do nothing and the program will exit with exit code 0 by default.
	If there is an issue we are using exit(1), so the program will exit with exit code 1.
	If there is something abnormal which is out of the running parameters of the program it will exit with exit code 2.

4. Please check the screenshots for reference, if you need more info please contact anyone of us from the group.


----------------------------
EXECUTING OUR CODE SANDALONE -- without professors server
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
