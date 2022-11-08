import csv
import sys



def fileValues(file):
    with open(file,'r') as csvFile:
        fileInput = csv.reader(csvFile)
        fileArray = []

        for n in fileInput:
            fileArray.append(n)

    return fileArray


def nodeNames(fileArray):
# just node names
    nodes = []
    for n in range(1,len(fileArray[0])):
        nodes.append(fileArray[0][n])
    return(nodes)

def main():
    file = sys.argv[1]
    letter = input("Please, provide the source node: ")
    fileArray = fileValues(file)
    nodeArray = nodeNames(fileArray)

    print(fileArray)
    print (nodeArray)

main()