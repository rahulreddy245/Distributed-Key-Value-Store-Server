import networkx as nx
import matplotlib.pyplot as plt

f = open("log.txt", "r")
opDict = {}
seqStartList = []
for line in f:
    seqStart, opcode, value, seqStop = line.split(",")
    seqStart = int(seqStart)
    opcode = int(opcode)
    value = int(value)
    seqStop = int(seqStop)
    opDict[seqStop] = [seqStart, opcode, value]
    seqStartList.append(seqStart)

seqStartList.sort();

DG = nx.DiGraph()


DG.add_nodes_from(seqStartList)

for i in range(1,len(seqStartList)):
    num = seqStartList[i]
    while(num > seqStartList[0]):
        num = num - 1
        if (num in opDict):
            seqStart = opDict[num][0]
            DG.add_edge(seqStart, seqStartList[i])
            break;

print(list(nx.simple_cycles(DG)))
nx.draw(DG)
plt.show()


