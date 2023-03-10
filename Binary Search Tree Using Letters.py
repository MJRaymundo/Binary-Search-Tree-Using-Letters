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

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
             if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.right
            
            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)

        return self

def build_tree(elements):
    print("Building tree with these elements:", elements)
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == '__main__':
    letters = ["M", "A", "R", "K", "J", "O", "H", "N", "M", "R", "A", "Y", "M", "U", "N", "D", "O"]
    letters_tree = build_tree(letters)
    print(letters_tree.in_order_traversal())
    print(letters_tree.search("K"))
    
    letter_to_delete = input("Enter the letter you want to delete: " )
    letters_tree.delete(letter_to_delete)
    print("After deleting " + letter_to_delete, letters_tree.in_order_traversal())