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
    return recur(previous, source, previous[current]) + current

#shortest path function using recur to find it
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
    P = {}
    #N'- set of nodes where least cost path known
    N = list(source)

    for currentNode in nodes:
        #if v adj to u
        if(cost[currentNode][source] != 9999):
            #then D(v) = c(u,v)
            D[currentNode] = cost[currentNode][source]
            P[currentNode] = source
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
                P[currentNode] = w

    P = shortestTree(P, source)

    return(D, P)

#creating the Node class
class Node:
    allNodes = {}

    def __init__(self, name, nodes):
        self.name = name
        
        self.Dx = self.Cx = {i:cost[name][i] for i in nodes}

        for i in nodes:
            self.Dv = {i:9999}

        self.Dv[self.name] = self.Dx
        self.adjacent = [i for i in self.Dx if i != name and self.Cx[i] != 9999]  

        Node.allNodes.update({name:self})
        self.updateDv()

#implementing Bellman-Ford algorithm to calculate distance vector
    def bellman(self,current):
        for node in self.Dx:
            temp = (self.Cx[current] + self.Dv[current][node]) # so doesn't need to rewrite it each time
            if (temp < self.Dx[node]):
                self.Dx[node] = (temp)
                self.updateDv()

    def updateDv(self):
        for node in self.adjacent:
            if node in Node.allNodes:
                current = Node.allNodes[node]
                self.Dv[current.name] = current.Dx
                self.bellman(current.name)

                current.Dv[self.name] = self.Dx
                current.bellman(self.name)

    def __str__(self):

        return ', '.join([str(self.Dx[i]) for i in self.Dx])

#implementing the distance vector function
def distanceVector(csvFile):
    return {i:Node(i, csvFile) for i in csvFile}

#main function
if __name__ == '__main__':
    file = sys.argv[1]
    source = input("Please, provide the source node: ")
    data = openCSV(file)
    data[0].remove("")
    heads = data[0]
    headList = ''.join(heads)
    #print(headList)
    #print(heads)
    cost = {i[0]:{heads[j]:int(i[1:][j]) for j in range(len(i[1:]))} for i in data[1:]}

    #calling Dijkstra's Algorithm
    D, P = dijAlg(data[0], source)
    tree = ', '.join(P.values())
    costs = ', '.join([f"{k}:{v}" for k,v in D.items()])

    #print statements
    print("Shortest path tree for node {}:\n {}".format(source, tree))
    print("Costs of least-cost paths for node {}:\n {}".format(source, costs))
    print("\nDistance vector for node {}:", costs)

    result = distanceVector(heads)
    for i in result:
        print(f"Distance vector for node {i}: {result[i]}")