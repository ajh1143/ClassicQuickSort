def quicksort(arr):
    #Initialize Lists
    pivoter = []
    highVal = []
    lowVal = []
    #Check size of list, if 1 or less, no need to sort, just return
    if len(arr) <= 1:
        return arr
    #Else, array contains items that must be sorted
    else:
        #Set pivot = first index
        pivot = arr[0]
        #For each element in arr, compare and append to higher/lower list or pivoter
        for i in arr:
            if i < pivot:
                lowVal.append(i)
            elif i > pivot:
                highVal.append(i)
            else:
                pivoter.append(i)
        low = quicksort(lowVal)
        high = quicksort(highVal)
        quickSorter = (low+pivoter+high)
    return quickSorter

x=quicksort([1,3,5,2])
print(x)
