import os
import sys
import json

def test():
    folder = '.'
    for count, filename in enumerate(os.listdir(folder)):
        if filename.endswith('.json'):
            theFile = open(filename, 'r')
            json_object = json.load(theFile)
            theFile.close()
            attributes = json_object["attributes"]
            newFile = open('rarity.csv',"w")
            for elem in attributes:
                nftNumber = filename.split('.')[0]
                traitType = elem["trait_type"]
                value = elem["value"]
                stringToCsv = f"{nftNumber},{traitType},{value}"
                newFile.write(stringToCsv)
            newFile.close()
            # theFile = open(filename, 'w')
            # json.dump(json_object, theFile)
            # theFile.close()

def main():
    test()

if __name__ == '__main__':
    main()