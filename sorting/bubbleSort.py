def bubbleSort(array):
    swap = True
    while swap:
        swap = False
        for items in range(len(array)-1):
            if array[items+1]:
                if array[items+1] < array[items]:
                    swap = True
                    array[items], array[items+1] = array[items+1], array[items]
    return array
            
arrs = [6,4, 8, 9, 2, 5]
print(arrs)
print(bubbleSort(arrs))