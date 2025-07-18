class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        NewNode = Node(value)
        if self.root == None:
            self.root = NewNode
        else:
            currentNode = self.root
            while True:
                if value<currentNode.value:
                    #Left
                    if not currentNode.left:
                        currentNode.left = NewNode
                        return self
                    currentNode = currentNode.left
                else:
                    #right
                    if not currentNode.right:
                        currentNode.right = NewNode
                        return self
                    currentNode = currentNode.right


    def lookup(self, value):
        currentNode = self.root
        while currentNode:
            if value == currentNode.value:
                return True
            elif value < currentNode.value:
                currentNode = currentNode.left
            else:
                currentNode = currentNode.right
        return False
    
    def remove(self, value):
        if not self.root:
            return False 
        currentNode = self.root
        parentNode = None

        while currentNode:
            if value < currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.left
            elif value > currentNode.value:
                parentNode = currentNode
                currentNode = currentNode.right
            else:
                # Option 1: No right child
                if not currentNode.right:
                    if not parentNode:
                        self.root = currentNode.left
                    else:
                        if currentNode.value < parentNode.value:
                            parentNode.left = currentNode.left
                        else:
                            parentNode.right = currentNode.left
                # Option 2: Right child with no left child
                elif not currentNode.right.left:
                    currentNode.right.left = currentNode.left
                    if not parentNode:
                        self.root = currentNode.right
                    else:
                        if currentNode.value < parentNode.value:
                            parentNode.left = currentNode.right
                        else:
                            parentNode.right = currentNode.right
                # Option 3: Right child with a left child
                else:
                    leftMost = currentNode.right.left
                    leftMostParent = currentNode.right
                    while leftMost.left:
                        leftMostParent = leftMost
                        leftMost = leftMost.left
                    leftMostParent.left = leftMost.right
                    leftMost.left = currentNode.left
                    leftMost.right = currentNode.right
                    if not parentNode:
                        self.root = leftMost
                    else:
                        if currentNode.value < parentNode.value:
                            parentNode.left = leftMost
                        else:
                            parentNode.right = leftMost
                return True
        return False




BST = BinarySearchTree()
BST.insert(5)
BST.insert(2)
BST.insert(10)


print(BST)
