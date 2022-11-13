import csv
import sys

def openCSV(file):
    with open(file,'r') as csvFile:
        fileInput = csv.reader(csvFile)
        fileArray = []

        for n in fileInput:
            fileArray.append(n)

    return fileArray

def recur(previous:dict, source:str, current:str):
    if current == source:
        return source
    return recur(previous, source, previous[current] + current)

def shortestTree(previous:dict, source:str):
    tree = {}
    for i in previous:
        #recur function requries previous, source, and current node
        tree[i] = recur(previous, source, i)
    return tree

#implementing Dijkstra's algorithm to calculate shortest path tree/
#cost of least cost path
def dijAlg(nodes:list, source:str):
    #recreating equation from slides
    #D(v)- current cost of least cost path
    D = {}
    #p(v)- previous node in path
    p = {}
    #N'- set of nodes where least cost path known
    N = list(source)

    for currentNode in nodes:
        #if v adj to u
        if(cost[currentNode][source] != 9999):
            #then D(v) = c(u,v)
            D[currentNode] = cost[currentNode][source]
            p[currentNode] = source
        else:
            #else D(v) = inf
            D[currentNode] = 9999

    currentNode = source

    #repeat algorithm
    while len(N) < len(nodes):
        #find w not in N'
        Dw = {k:v for k,v in D.items() if k not in N}
        w = min(Dw, key = Dw.get)
        N.append(w)

        exNodes = [i for i in nodes if i not in N]
        for currentNode in exNodes:
            #D(v) = minimum of D(v) and D(w) + c(w,v)
            nextD = min(D[currentNode], (D[w] + cost[w][currentNode]))
            if(nextD != D[currentNode]):
                D[currentNode] = nextD
                p[currentNode] = w

    p = shortestTree(p, source)

    return(D, p)

#creating the Node class



class Node:
    allNodes = {}

    def __init__(self, name, nodes):
        self.name = name

        #for i in nodes:
            #self.Dx = self.Cx = cost[name][i]
        self.Dx = self.Cx = {i:cost[name][i] for i in nodes}


        INF = {i:9999 for i in nodes}
        self.Dv = {i:INF for i in nodes}
        self.Dv[self.name] = self.Dx
        self.adjacent = [i for i in self.Dx if i != name and self.Cx[i] != 9999]
        


        Node.allNodes.update({name:self})
        self.updateDv()

#implementing Bellman-Ford algorithm to calculate distance vector
    def bellFord(self,current):
        for node in self.Dx:
            if (self.Cx[current]+self.Dv[current][node] < self.Dx[node]):
                self.Dx[node] = (self.Cx[current]+self.Dv[current][node])
                self.updateDv()

    def updateDv(self):
        for node in self.adjacent:
            if node in Node.allNodes:
                currentNode = Node.allNodes[node]
                self.Dv[currentNode.name] = currentNode.Dx
                self.bellFord(currentNode.name)

                currentNode.Dv[self.name] = self.Dx
                currentNode.bellFord(self.name)

    def __str__(self):
        return ', '.join([str(self.Dx[i]) for i in self.Dx])

#implementing the distance vector function
def distanceVector(csvFile:list):
    return {i:Node(i, csvFile) for i in csvFile}

#main function
if __name__ == '__main__':
    file = sys.argv[1]
    source = input("Please, provide the source node: ")
    data = openCSV(file)
    data[0].remove("")
    header = data[0]
    cost = {i[0]:{header[j]:int(i[1:][j]) for j in range(len(i[1:]))} for i in data[1:]}

    #calling Dijkstra's Algorithm
    #D, p = dijAlg(data[0], source)
    #tree = ', '.join(p.values())
    #costs = ', '.join([f"{k}:{v}" for k,v in D.items()])

    #print statements
    #print("Shortest path tree for node {}:\n {}".format(source, tree))
    #print("Costs of least-cost paths for node {}:\n {}".format(source, costs))
    #print("\nDistance vector for node {}:", distance)

    result = distanceVector(header)
    for i in result:
        print(f"Distance vector for node {i}: {result[i]}")
