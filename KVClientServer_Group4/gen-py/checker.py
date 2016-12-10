import networkx as nx
import time
#import matplotlib.pyplot as plt
import sys


# Used to hold the directed graphs
DG = nx.DiGraph()

theFile = open("log.txt", "r")
# We use this dictionary for building the Time edges
opDict = {}
# We use this dictionary for building the Data edges
valueDict = {}
# We might need this for hybrid
FILE = theFile.readlines()
# We use this dictionary for building the Time edges along with the opDict
seqStartList = []
# Readop dict
readop = {}
# WriteOP dict
writeop = {}

def pathexists(G,source,target):
    #print("checking for path")
    for path in nx.all_simple_paths(G,source,target,4):
        #print("still checking")
        return True  #if it finds one, it returns True, and gets out of the function.  It doesn't look for the next.
    return False  #if it didn't find one, it gets out of the function.


def main(argv):

    for line in FILE:
        seqStart, opcode, value, seqStop = line.split(",")
        seqStart = int(seqStart)
        opcode = int(opcode)
        value = int(value)
        seqStop = int(seqStop)
        opDict[seqStop] = [seqStart, opcode, value]
        if opcode == 0:
            seqStartList.append((seqStart, "W"))
            valueDict[value] = [seqStart, seqStop]
            nodestruct = 'W:{0}'.format(str(seqStart))
            DG.add_node(nodestruct)
            writeop[nodestruct] = value
        if opcode == 1:
            seqStartList.append((seqStart, "R"))
            nodestruct = 'R:{0}'.format(str(seqStart))
            DG.add_node(nodestruct)
            readop[nodestruct] = value
            # We add the edge as and when there is a read
            # to its the write from which this value was written
            if value in valueDict.keys():
                tempseqstart = valueDict[value][0]
                edgestart = 'W:{0}'.format(str(tempseqstart))
                if DG.has_node(edgestart):
                    DG.add_edge(edgestart, nodestruct)
                else:
                    print("Something wrong!")
            else:
                if value ==0:
                    continue
                print("Failing because of :"+str(value))
                #exit(1)
                continue
            # You have to process hybrid Edges here
            #

    seqStartList.sort()

    for i in range(1,len(seqStartList)):
        num = seqStartList[i][0]
        op = seqStartList[i][1]
        while num > seqStartList[0][0]:
            num -= 1
            if num in opDict:
                seqStart = opDict[num][0]
                opcode = opDict[num][1]
                if opcode == 0:
                    DG.add_edge('W:{0}'.format(str(seqStart)), op + ":" + str(seqStartList[i][0]))
                else:
                    DG.add_edge('R:{0}'.format(str(seqStart)), op + ":" + str(seqStartList[i][0]))
                break

    print("Time and data edge complete")
#    for e in writeop:
    for r in readop:
        rstart = int(r.split(":")[1])
        value = readop[r]
        if value in valueDict:
            wstart = valueDict[value][0]

            for i in range(wstart+1, rstart):
                e = "W:{0}".format(i)
                if e in writeop:
                    #print(rstart, wstart, e)
                    if pathexists(DG, e, r):
                        print("this works")
                        print (wstart, rstart, e)
                        #get value from the readop edge
                        #value = readop[r]

                        #if value in valueDict.keys():
                        print("Hybrid")
                        tempseqstart = valueDict[value][0]
                        edgestart = 'W:{0}'.format(str(tempseqstart))
                        if DG.has_node(edgestart):
                            DG.add_edge(e,edgestart)

    print(list(nx.simple_cycles(DG)))
    print (DG.number_of_edges())

#    print (len(writeop)+len(readop))
    #nx.draw(DG)
    #plt.show()

if __name__ == "__main__":
    try:
        start = time.time()
        main(sys.argv)
        stop = time.time()
        print(stop - start)
    except Exception as e:
        sys.stderr.write("Error: "+str(e))
        print(e)
        sys.exit(2)

