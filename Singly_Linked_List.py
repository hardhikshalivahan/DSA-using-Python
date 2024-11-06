# Singly Linked List (SLL) Implementation

# Node class to represent each element in the linked list
class Node:
    def __init__(self, value=None, nex=None):
        self.value = value  
        self.nex = nex     

# Singly Linked List class with various operations
class SLL:
    def __init__(self, start=None):
        self.start = start  

    # Method to check if the linked list is empty
    def empty(self):
        return self.start is None  

    # Method to insert a node at the start of the linked list
    def insert_start(self, value):
        n = Node(value, self.start)  
        self.start = n 

    # Method to insert a node at the end of the linked list
    def insert_end(self, value):
        n = Node(value)  
        if self.empty():  
            self.start = n 
        else:
            temp = self.start  
            while temp.nex is not None: 
                temp = temp.nex
            temp.nex = n  

    # Method to search for a node with a specific value
    def search(self, value):
        temp = self.start  
        while temp is not None:  
            if temp.value == value:  
                return temp  
            temp = temp.nex  
        return None  

    # Method to insert a node after a node with a specific value
    def insert_after(self, temp_value, value):
        s = self.search(temp_value)  
        if s is not None:  
            n = Node(value, s.nex)
            s.nex = n  

    # Method to display the elements of the linked list
    def display(self):
        a = self.start  
        while a is not None:  
            print(a.value, end=' ') 
            a = a.nex 
        print()  

    # Method to delete the first node of the linked list
    def delete_first(self):
        if self.start is not None:  
            self.start = self.start.nex  

    # Method to delete the last node of the linked list
    def delete_last(self):
        if self.start is None: 
            return
        elif self.start.nex is None: 
            self.start = None  
        else:
            temp = self.start  
            while temp.nex and temp.nex.nex is not None: 
                temp = temp.nex
            temp.nex = None  
    # Method to delete a specific element by value
    def delete_ele(self, value):
        if self.start is None:  
            return
        if self.start.value == value:  
            self.start = self.start.nex  
            return
        temp = self.start 
        while temp.nex is not None:  
            if temp.nex.value == value:  
                temp.nex = temp.nex.nex  
                return
            temp = temp.nex  

    # Iterator method to allow for easy traversal of the list using a for loop
    def __iter__(self):
        return LinkedListIterator(self.start) 
    
# Custom iterator class for Linked List traversal
class LinkedListIterator:
    def __init__(self, start):
        self.curr = start  

    def __iter__(self):
        return self

    def __next__(self):
        if not self.curr: 
            raise StopIteration
        data = self.curr.value  
        self.curr = self.curr.nex  
        return data  # Return the value of the current node


# Test code: creating and manipulating the linked list
l = SLL()  # Create an empty linked list
# Inserting elements...
l.insert_start(8)  
l.insert_start(5)  
l.insert_start(11)  
l.insert_end(58) 
l.insert_after(5, 38)  # Insert 38 after the node with value 5

# Display the original list
print("---Original Node:")
l.display()

# Delete the first node
l.delete_first()
print("---Deleted First Element:")
l.display()

# Delete the last node
l.delete_last()
print("---Deleted Last Element:")
l.display()

# Recreate the original node by inserting 11 and 58 again
l.insert_start(11)
l.insert_end(58)
print("---Reformed Original Node:")
l.display()

# Delete the element with value 38
l.delete_ele(38)
print("---Deleted Element 38:")
l.display()

# Iterate over the list using the iterator
for h in l:
    print(h, end=" ")