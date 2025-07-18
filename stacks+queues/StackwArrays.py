class Stack:
    def __init__(self):
        self.array = []

    def peek(self):
        return self.array[len(self.array)-1]

    def push(self,value):
        self.array.append(value)
        return self

    def pop(self):
        self.array.pop()
        return self

myStack = Stack()
myStack.push(2)
myStack.push(10)
print(myStack.peek())
myStack.pop()
print(myStack.peek())