class Graph:
    def __init__(self):
        self.numNodes = 0
        self.adjacentList = {}

    def addVertex(self, node):
        self.adjacentList[node] = []
        self.numNodes +=1

    def addEdge(self, node1, node2):
        self.adjacentList[node1].append(node2)
        self.adjacentList[node2].append(node1)
        

    def showConnections(self):
        AllNodes = self.adjacentList.keys()
        for node in AllNodes:
            NodeConnection = self.adjacentList[node]
            connections = ""
            for vertex in NodeConnection:
                connections += str(vertex) + " "
            print(str(node) + " --> " + connections)

myGraph = Graph()
myGraph.addVertex('0')
myGraph.addVertex('1')
myGraph.addVertex('2')
myGraph.addVertex('3')
myGraph.addVertex('4')
myGraph.addVertex('5')
myGraph.addVertex('6')
myGraph.addEdge('1','2')

myGraph.showConnections()