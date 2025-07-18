#10 --> 5 --> 15
myLinkedList = {
    "head": {
        "value": 10,
        "next": {
            "value": 5,
            "next": {
                "value": 15,
                "next": None
            }
        }
    }
}

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class linkedList:
    def __init__(self, value):
        newNode = Node(value)
        self.head = newNode
        self.tail = newNode
        self.length = 1

    def append(self, value):
        newNode = Node(value)
        self.tail.next = newNode
        self.tail = newNode
        self.length += 1
        return self

    def prepend(self, value):
        newNode = Node(value)
        newNode.next = self.head
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
        newNode.next = leader.next
        leader.next = newNode
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
        leader.next = self.traverse(index+1)
        self.length -=1

    def reverse(self):
        if not self.head.next:
            return self.head
        first = self.head
        self.tail = self.head
        second = first.next
        while second:
            temp = second.next
            second.next = first
            first = second
            second = temp
        self.head.next = None
        self.head = first
        return self
            


LL = linkedList(10)
LL.append(5)
LL.append(16)
LL.prepend(1)
LL.insert(2, 70)
LL.insert(99, 4)
LL.insert(0, 44)
LL.remove(3)
print(LL.printList())
print(LL.reverse().printList())
