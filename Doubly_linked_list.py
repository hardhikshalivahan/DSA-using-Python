# Doubly Linked List (DLL) Implementation

# Node for the doubly linked list has three fields: prev, value, and next.
class Node:
    def __init__(self, prev=None, value=None, nex=None):
        self.prev = prev  # Pointer to the previous node
        self.value = value  # Data stored in the node
        self.nex = nex  # Pointer to the next node

class DLL:
    # Doubly Linked List class with methods for insertion, deletion, and traversal
    def __init__(self, start=None):
        self.start = start  # Points to the head (start) of the DLL

    # Method to insert a node at the start of the linked list
    def insert_first(self, value):
        n = Node(value=value, nex=self.start)  
        if self.start is not None:
            self.start.prev = n 
        self.start = n  

    # Method to insert a node at the end of the linked list
    def insert_last(self, value):
        n = Node(value=value)  
        if self.start is None: 
            self.start = n
        else:
            temp = self.start
            while temp.nex is not None:
                temp = temp.nex
            temp.nex = n  
            n.prev = temp  

    # Method to insert a node after a perticular node in the linked list
    def insert_after(self, ele, value):
        temp = self.start
        while temp is not None and temp.value != ele:
            temp = temp.nex
        if temp is not None:
            n = Node(prev=temp, value=value, nex=temp.nex) 
            if temp.nex is not None:
                temp.nex.prev = n  
            temp.nex = n 

    # Method to insert a node before a perticular node in the linked list
    def insert_before(self, ele, value):
        temp = self.start
        while temp is not None and temp.value != ele:
            temp = temp.nex
        if temp is not None:
            n = Node(prev=temp.prev, value=value, nex=temp)
            if temp.prev is not None:
                temp.prev.nex = n  
            else:
                self.start = n  
            temp.prev = n  

    # Method to first node in the linked list
    def delete_first(self):
        if self.start is not None:
            self.start = self.start.nex  
            if self.start is not None:
                self.start.prev = None  
    
    # Method to first node in the linked list
    def delete_last(self):
        if self.start is None:  
            return
        temp = self.start
        while temp.nex is not None:
            temp = temp.nex
        if temp.prev is not None:
            temp.prev.nex = None  
        else:
            self.start = None  

    # Method to delete an element in the Linkedlist
    def delete_ele(self, ele):
        temp = self.start
        while temp is not None:
            if temp.value == ele:
                if temp.prev is not None:
                    temp.prev.nex = temp.nex  
                else:
                    self.start = temp.nex  
                if temp.nex is not None:
                    temp.nex.prev = temp.prev  
                break
            temp = temp.nex

    # Method to Search for an element in the Linkedlist
    def search(self, ele):
        temp = self.start
        while temp is not None:
            if temp.value == ele:
                print(f"{ele} Found")
                return
            temp = temp.nex
        print(f"{ele} Not Found")

    # Method to Display the elements of the Linkedlist
    def display(self):
        temp = self.start
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.nex
        print() 

    # Return an iterator object for the list to allow iteration using for-loops.
    def __iter__(self):
        return DLLIterator(self.start)

class DLLIterator:

    # Custom iterator for traversing the DLL
    def __init__(self, start):
        self.curr = start 

    def __iter__(self):
        return self  # Return the iterator object itself

    def __next__(self):
        if self.curr is None:
            raise StopIteration  
        data = self.curr.value 
        self.curr = self.curr.nex  
        return data

# Test the DLL implementation
h = DLL()

# Inserting at the start
h.insert_first(11)
h.insert_first(8)
h.insert_first(5)
print("---Inserted first elements")
h.display()

# Inserting at the last
h.insert_last(58)
h.insert_last(85)
print("---Inserted last elements")
h.display()

# Inserting after an element
h.insert_after(8, 23)
print("---Inserted after 8")
h.display()

# Inserting before an element
h.insert_before(5, 17)
print("---Inserted before 5")
h.display()

# Searching for elements
print("---Search for element 45:")
h.search(45)
print("---Search for element 11:")
h.search(11)

# Deleting elements
h.delete_first()
print("---Deleted first element")
h.display()

h.delete_last()
print("---Deleted last element")
h.display()

h.delete_ele(58)
print("---Deleted element 58")
h.display()

# Iterating over the list
print("---Iterating over the list:")
for l in h:
    print(l, end=" ")