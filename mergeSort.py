#Jonathan Hooper MergeSort Jan 2017
import time
import random

#merge function, should compare 2 lists, taking smallest from each side.

fullList = []
for i in range(0,10000):
    fullList.append(random.randint(0,10000))
startTime = time.time()

def merge(left,right):
    mergedList = []
    while len(left) != 0 and len(right) != 0:
        if left[0] <= right[0]:
            mergedList.append(left[0])
            left.remove(left[0])
        else:
            mergedList.append(right[0])
            right.remove(right[0])
    return mergedList + left + right

def mergeSort(uList):
    if len(uList) < 2:
        return uList
    mid = len(uList)//2
    left = mergeSort(uList[:mid])
    right = mergeSort(uList[mid:])
    return merge(left,right)

sortedList = mergeSort(fullList)
endTime = time.time()
totalTime = endTime - startTime
listLen = len(fullList)
print(sortedList)
print(str(listLen),'items merge sorted in',str(totalTime), 'seconds')
