import csv
import sys


file = sys.argv[1]
letter = input("Please, provide the source node: ")

with open(file,'r') as csvFile:
    fileInput = csv.reader(csvFile)
    fileArray = []

    for n in fileInput:
        fileArray.append(n)

nodes = []
for n in range(len(fileArray[0])):
    nodes.append(fileArray[0][n])

print(nodes)