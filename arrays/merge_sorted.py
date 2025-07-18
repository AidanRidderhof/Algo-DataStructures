def mergeSortedArrays(arr1, arr2):
    if len(arr1) == 0:
        return arr2
    if len(arr2) == 0:
        return arr1

    arr1item = arr1[0]
    arr2item = arr2[0]
    i = 1
    j = 1

    mergedArr = []
    while arr1item is not None or arr2item is not None:
        if arr2item is None or (arr1item is not None and arr1item < arr2item):
            mergedArr.append(arr1item)
            if i < len(arr1):
                arr1item = arr1[i]
                i += 1
            else:
                arr1item = None
        else:
            mergedArr.append(arr2item)
            if j < len(arr2):
                arr2item = arr2[j]
                j += 1
            else:
                arr2item = None
    return mergedArr


#mergedArr = arr1+arr2
#mergedArr.sort

print(mergeSortedArrays([0, 3, 4, 31], [4, 6, 30]))