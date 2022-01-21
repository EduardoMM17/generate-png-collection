import os
import sys
import csv
from utils import bubbleSortForFiles

def getFileHeader():
    folder = sys.argv[1]
    headers = []
    for count, filename in enumerate(os.listdir(folder)):
        fileNameSplitted = filename.split('_')
        column = fileNameSplitted[1]
        headers.append(column)
    headers = list(dict.fromkeys(headers))
    return headers

def getFilesNames():
    folder = sys.argv[1]
    newList = []
    for count, filename in enumerate(os.listdir(folder)):
        newList.append(filename)
    return newList

def getData(headers, filesSorted):
    data = []
    currentRow = 1
    rowData = fillRowDataWithHyphen(len(headers))
    for j in range(len(filesSorted)):
        filename = filesSorted[j]
        fileNameSplitted = filename.split('_')
        row = fileNameSplitted[0]
        layer = fileNameSplitted[1]
        description = fileNameSplitted[2].split('.')[0]
        if int(row) != currentRow:
            currentRow = int(row)
            data.append(rowData)
            rowData = fillRowDataWithHyphen(len(headers))    
        for i in range(len(headers)):
            header = headers[i]
            if header == layer:
                rowData[i] = description
                break
        if(j == len(filesSorted)-1):
            data.append(rowData)
    return data

def fillRowDataWithHyphen(headersLen):
    newList = []
    for i in range(headersLen):
        newList.append('-')
    return newList

def writeToCsvFile(headers, data):
    with open('traits_and_layers.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(data)

def main():
    headers = getFileHeader()
    files = getFilesNames()
    bubbleSortForFiles(files)
    data = getData(headers,files)
    writeToCsvFile(headers,data)


if __name__ == '__main__':
    main()
