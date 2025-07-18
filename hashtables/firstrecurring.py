def firstrecurring(input):
    seen = {}
    for i in input:
    #for i in range(len(input)):
        if i in seen:
        #if input[i] in seen:
            return i
        else:
            seen[i] = True
            #seen[input[i]] = True
    return False

print(firstrecurring([2,5,1,2,3,5,1,2,4]))