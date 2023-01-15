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

    def in_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.in_order_traversal()
        
        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False


def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == '__main__':
    letters = ["M", "A", "R", "K", "J", "O", "H", "N", "M", "R", "A", "Y", "M", "U", "N", "D", "O"]
    letters_tree = build_tree(letters)
    print(letters_tree.in_order_traversal())
    print(letters_tree.search("K"))