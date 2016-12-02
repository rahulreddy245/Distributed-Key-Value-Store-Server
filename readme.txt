-------------------------											
README : Key-Value Store
-------------------------

------------
INTRODUCTION
------------
We have developed our code in Python 2.7 and used Thrift-0.9.3 library. The program has a server called kvserver.py and a client called kvclient.py which uses the kvstore.py, generated from the thrift file, as a communication mechanism.

-------------------
EXECUTING OUR CODE
-------------------
Please follow the steps in prerequisites section before executing this code.
1. Unzip the project folder we sent you and navigate to path in command line: /"path to project folder"/gen-py/.
2. Running Server: First, run the kvserver.py using command python kvserver.py. This should print the hostname to the terminal.
3. Running Client: Now open another terminal at the same location, run the command
4. For running client on Unix/Linux/Mac execute the following command on the command shell,
./kvclient -server localhost:9090 -set a apple
./kvclient -server localhost:9090 -get a 
./kvclient -server localhost:9090 -del a 
5. For running client on Windows execute the following command on the command shell,
 python ./kvclient -server localhost:9090 -set a apple
6. Please check the screenshots if you need more help in execution or anyone of contact us

---------------
PRE-REQUISITES
---------------
Please follow the following steps before running the project.
1. Install Python 2.7 to your PC. 
2. Download the thrift repository from github. Link- https://github.com/apache/thrift (Not the exe, but the actual repository).
3. Using the command prompt, navigate to the directory, /"path to thrift folder"/lib/py/.  You should have setup.py file present in that folder.
4. Use the command python setup.py install on the command line. (This should install the thrift python libraries)
5. Now navigate to the project folder /"path to project folder"/gen-py/.

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
