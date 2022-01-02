unSortedList = [5,2,8,4,10,1,3]
#0,1,2,3,4,5,8

### BUBBLESORT ###

#Time Complexity: Worst: O(n^2) list sorted least to greatest, Best: O(n) list already sorted
def bubbleSort(yourList):
    for x in range(len(yourList)): # goes through the entire list

        for y in range(0, (len(yourList) - x - 1)): # goes through the the list - x each time

            if(yourList[y] > yourList[y+1]): # if pointer 1 > pointer 2 swap them
                yourList[y], yourList[y+1] = yourList[y+1], yourList[y]
    return(yourList)

### INSERTIONSORT ###

def insertionSort(yourList):
    for x in range(len(yourList)): # goes through the entire list
        y = x
        while(y > 0):
            print(y, yourList)
            if(yourList[y-1] > yourList[y]): # if pointer 1 > pointer 2 swap them
                yourList[y-1], yourList[y] = yourList[y], yourList[y-1]

            else:
                y = 0

            y = y-1
            
    return(yourList)

### MERGESORT ###

def merge(left, right):
    print("Merging...", left, right)
    if(len(left) == 0):
        return(right)

    elif(len(right) == 0):
        return(left)

    else:
        if(left[0] > right[0]):
            return([right[0]] + merge(left, right[1:]))
        else:
            return([left[0]] + merge(left[1:], right))


def mergeSort(yourList):
    print("Sorting...", yourList)
    if(len(yourList) == 1): # if the list only has one value then it is already sorted
        print("Boom", yourList)
        return(yourList)
    else:
        mid = len(yourList) // 2 # split the list at the middle point
        print(yourList[:mid], yourList[mid:])
        left = mergeSort(yourList[:mid]) # take the left list and sort it
        right = mergeSort(yourList[mid:]) # take the right side of the list and sort it
        return(merge(left, right))

### QUICKSORT ###

def partition(yourList, low, high):
    print(yourList)
    #the rightmost item is the pivot
    pivot = yourList[high]
    print("Pivot", pivot)

    #pointer for holding the greater element
    greaterIndex = low - 1

    for x in range(low, high):
        print(yourList)
        if yourList[x] <= pivot:
            greaterIndex += 1
            print("Swapping", yourList[greaterIndex], yourList[x])
            yourList[greaterIndex], yourList[x] = yourList[x], yourList[greaterIndex]

    #Place pivot in sorted position
    yourList[greaterIndex + 1], yourList[high] = yourList[high], yourList[greaterIndex + 1]
    print("Sort Pivot", yourList)
    return (greaterIndex + 1)

def quickSort(yourList, low, high):
    print(low, high)
    if low < high:
        #find the pivot point
        pivot = partition(yourList, low, high)
        print(pivot)

        #left side of the list
        quickSort(yourList, low, pivot - 1)
        #right side of the list
        quickSort(yourList, pivot + 1, high)
    return(yourList)




#print("Bubble Sort",bubbleSort(unSortedList))
#print("Insertion Sort",insertionSort(unSortedList))
#print("Merge Sort",mergeSort(unSortedList))
print("Quick Sort", quickSort(unSortedList, 0, (len(unSortedList) - 1)))
        

