def bubbleSortForFiles(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            index = int(arr[j].split('_')[0])
            nextElemIndex = int(arr[j+1].split('_')[0])
            if(index > nextElemIndex):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]