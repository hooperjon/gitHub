#Jonathan Hooper MergeSort Jan 2017

#merge function, should compare 2 lists, taking smallest from each side.
fullList = [10,7,5,2,3,9,1,4,6,8]


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
    mList = merge(left,right)
    return mList


sortedList = mergeSort(fullList)
print(sortedList)