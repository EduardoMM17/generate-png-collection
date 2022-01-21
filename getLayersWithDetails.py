def readFile():
    lineCount = 1
    f = open('layers_traits_quantities.csv','r')
    rowDict = {}
    for line in f:
        line = line.rstrip()
        if lineCount == 1:
            headers = line.split(',,')
        elif lineCount > 2:
            rowElem = line.split(',')
            rowDict[lineCount-2] = []
            trait = ''
            quantity = ''
            for i in range(len(rowElem)):
                elem = rowElem[i]
                if(i % 2 == 0):
                    trait = elem
                else:
                    quantity = elem
                if(trait != '' and quantity != ''):
                    rowDict[lineCount-2].append({'Trait': trait, 'Quantity': quantity})
                    trait = ''
                    quantity = ''
        lineCount +=1 
    return headers, rowDict

def buildLayersDict():
    headers, rows = readFile()
    newDic = {}
    for i in range(len(headers)):
        newDic[headers[i]] = []
        for key in rows:
            trait = rows[key][i]['Trait']
            quantity = rows[key][i]['Quantity']
            if(trait != '-'):
                newDic[headers[i]].append({'Trait': trait, 'Quantity': quantity})
    return newDic