class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def peek(self):
        return self.top.value

    def push(self,value):
        newNode = Node(value)
        if self.length == 0:
            self.bottom = newNode
            self.top = newNode
        else:
            holdingPointer = self.top
            self.top = newNode
            self.top.next = holdingPointer
        self.length+=1
        return self

    def pop(self):
        if not self.top:
            return None
        if self.top == self.bottom:
            self.bottom = None
        #holdingPointer = self.top
        self.top = self.top.next
        self.length -= 1
        return self

myStack = Stack()
myStack.push(2)
myStack.push(10)
print(myStack.peek())
myStack.pop()
print(myStack.peek())