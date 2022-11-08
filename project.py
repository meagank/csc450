import csv
import sys



def getValues(file):
    with open(file,'r') as csvFile:
        fileInput = csv.reader(csvFile)
        data = []

        for n in fileInput:
            data.append(n)

        data[0].remove("")
        names = data[0]

    return data,names


def main():
    file = sys.argv[1]
    letter = input("Please, provide the source node: ")
    data,names = getValues(file)

    print(data)
    print(names)

main()