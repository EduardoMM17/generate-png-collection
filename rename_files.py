import os
import sys

def main():
    folder = sys.argv[1]
    for count, filename in enumerate(os.listdir(folder)):
        fileNameSplitted = filename.split('_')
        layer = fileNameSplitted[0]
        number = count + 1
        if(len(fileNameSplitted) > 2):
            description = fileNameSplitted[2].split('.')[0]
            if description != '':
                dst = f"{number}_{folder}_{description}.png"
            else:
                numberString = getNumberAsString(count)
                dst = f"{number}_{folder}_{numberString}.png"
        else:
            numberString = getNumberAsString(number)
            dst = f"{number}_{folder}_{numberString}.png"

        src = f"{folder}/{filename}"
        dst = f"{folder}/{dst}"
        os.rename(src,dst)


def getNumberAsString(number):
    numbers = ['one','two','three','four','friday','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen']
    return numbers[number-1]


if __name__ == '__main__':
    main()
