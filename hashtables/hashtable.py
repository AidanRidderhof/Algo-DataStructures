class hashTable:
    def __init__(self, size):
        self.data = [None] * size

    def _hash(self, key): 
        hash = 0
        for i in range(len(key)):
            hash = (hash + ord(key[i]) * i) % len(self.data)

        return hash
    
    def set(self, key, value):
        address = self._hash(key)
        if not self.data[address]:
            self.data[address] = []
        self.data[address].append([key, value])
        return self.data
    
    def get(self,key):
        address = self._hash(key)
        currentBucket = self.data[address]
        if currentBucket:
            for i in range(len(currentBucket)):
                if currentBucket[i][0] ==key:
                    return currentBucket[i][1]
        return None
    
    def keys(self):
        keysArray = []
        for i in range(len(self.data)):
            if self.data[i]:
                keysArray.append(self.data[i][0][0])

        return keysArray

myHashTable = hashTable(50)
myHashTable.set('grapes', 10000)
myHashTable.set('oranges', 67)
myHashTable.set('apples', 33)
print(myHashTable.get('apples'))
print(myHashTable.keys())