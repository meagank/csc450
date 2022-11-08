import csv
import sys



def getValues(file):
    with open(file,'rt') as csvFile:
        fileInput = csv.reader(csvFile)
        fileArray = []

        for n in fileInput:
            fileArray.append(n)

        nodes = []
        for n in range(1,len(fileArray[0])):
            nodes.append(fileArray[0][n])

    return fileArray,nodes


def main():
    file = sys.argv[1]
    letter = input("Please, provide the source node: ")
    data,nodes = getValues(file)

    print(data)

main()