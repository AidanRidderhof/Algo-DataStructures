class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0
    
    def peek(self):
        return self.first.value
    
    def enqueue(self, value):
        newNode = Node(value)
        if self.length == 0:
            self.first = newNode
            self.last = newNode
        else:
            self.last.next = newNode
            self.last = newNode
        self.length += 1
        return self
    
    def dequeue(self):
        if not self.first:
            return None
        if (self.first == self.last):
            self.last = None
        removed = self.first
        self.first = self.first.next
        self.length -= 1
        return removed.value
    
myQueue = Queue()
myQueue.enqueue(2)
print(myQueue.peek())
myQueue.enqueue(7)
myQueue.enqueue(14)
myQueue.dequeue()
print(myQueue.peek())
