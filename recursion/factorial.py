def findFactorialRecursive(num):
    if num!=1:
        return num * findFactorialRecursive(num-1)
    return 1
print(findFactorialRecursive(5))