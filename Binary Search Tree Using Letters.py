# Mark john M. Raymundo CoE 2-2 Data Structure and Algorithms
# Instructions: Create a demo using the letters in your fullname as the content of the binary tree. 
# Source: Part 1 https://www.youtube.com/watch?v=lFq5mYUWEBk Part 2 https://www.youtube.com/watch?v=JnrbMQyGLiU

class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def add_child(self, data):
    if data == self.data:
        return

    if data < self.data:
        if self.left:
            self.left.add_child(data)
        else:
            self.left = BinarySearchTreeNode(data)
    else:
        if self.right:
            self.right.add_child(data)
        else:
            self.right = BinarySearchTreeNode(data)