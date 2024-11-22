# Implementation of Binary search Tree

# Node class represents each individual node in the Binary Search Tree
class node:
    def __init__(self, left=None, value=None, right=None):
        self.left = left  # Left child
        self.value = value  # Node value
        self.right = right  # Right child

# BST class to manage tree operations like insertion, traversal, deletion, and search
class har:
    def __init__(self):
        self.root = None 

    # Method to insert a value into the BST (Iterative insertion)
    def insert(self, value):
        n = node(value=value) 
        if self.root is None: 
            self.root = n
        else:
            temp = self.root 
            while True:
                if temp.value > value: 
                    if temp.left is None:  
                        temp.left = n
                        break
                    else:  
                        temp = temp.left
                else:  
                    if temp.right is None:  
                        temp.right = n
                        break
                    else:  
                        temp = temp.right

    # Method to display the BST using inorder traversal
    def display(self):
        self.inorder(self.root) 

    # Helper method for recursive inorder traversal
    def inorder(self, node):
        if node is not None:
            self.inorder(node.left) 
            print(node.value, end=" ") 
            self.inorder(node.right)  

    # Method to search for a value in the BST
    def search(self, value):
        return self.search_ele(self.root, value) 

    # Helper method for recursive search
    def search_ele(self, node, value):
        if node is None: 
            return (value, "not found")
        elif node.value == value:  
            return (node.value, "Yes Found")
        elif node.value > value:  
            return self.search_ele(node.left, value)
        else: 
            return self.search_ele(node.right, value)

    # Method to delete a node from the BST
    def delete(self, ele):
        self.root = self.delete_ele(self.root, ele) 

    # Helper method for recursive deletion
    def delete_ele(self, root, ele):
        if root is None:  
            print(ele, "not found")
        elif root.value > ele: 
            root.left = self.delete_ele(root.left, ele)
        elif root.value < ele: 
            root.right = self.delete_ele(root.right, ele)
        else:  
            if root.left is None:
                return root.right
            elif root.right is None:  
                return root.left
            else: 
                root.value = self.maximum(root.left)  
                root.left = self.delete_ele(root.left, root.value) 
        return root 

    # Method to find the maximum value in a subtree
    def maximum(self, root):
        while root.right:  
            root = root.right
        return root.value 

# Example usage of the BST
l = har()
l.insert(11)
l.insert(5)
l.insert(17)
l.insert(23)
l.insert(8)
l.insert(58)
l.display()  # Display the BST in sorted order
print()
print(l.search(11))  # Search for value 11
print(l.search(58))  # Search for value 58
print()
l.delete(11)  # Delete the node with value 11
l.display()  # Display the BST after deletion