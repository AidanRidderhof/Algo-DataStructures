class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None



class doublyLinkedList:
    def __init__(self, value):
        newNode = Node(value)
        self.head = newNode
        self.tail = newNode
        self.length = 1

    def append(self, value):
        newNode = Node(value)
        newNode.prev=self.tail
        self.tail.next = newNode
        self.tail = newNode
        self.length += 1
        return self

    def prepend(self, value):
        newNode = Node(value)
        newNode.next = self.head
        self.head.prev = newNode
        self.head = newNode
        self.length += 1
        return self
    
    def printList(self):
        array = []
        currentNode = self.head
        while currentNode:
            array.append(currentNode.value)
            currentNode = currentNode.next
        return array

    def traverse(self, index):
        currentNode = self.head
        for i in range(index):
            currentNode = currentNode.next
        return currentNode
    
    def insert(self, index, value):
        if index >= self.length:
            return self.append(value)
        elif index<=0:
            return self.prepend(value)
        newNode = Node(value)
        leader = self.traverse(index-1)
        follower = leader.next
        leader.next = newNode
        newNode.prev = leader
        newNode.next = follower
        self.length+=1
        return self

        # currentNode = self.head
        # for i in range(index):
        #     if i == index-1:
        #         newNode.next = currentNode.next
        #         currentNode.next=newNode
        #     else:
        #         currentNode=currentNode.next

    def remove(self, index):
        leader = self.traverse(index-1)
        follower = self.traverse(index+1)
        leader.next = follower
        follower.prev = leader
        self.length -=1
                

LL = doublyLinkedList(10)
LL.append(5)
LL.append(16)
LL.prepend(1)
LL.insert(2, 70)
LL.remove(3)
print(LL.printList())