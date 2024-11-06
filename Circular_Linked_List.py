# Node class for Circular Linked List
class node:
    def __init__(self, value=None, nex=None):
        self.value = value  
        self.nex = nex      

# Circular Linked List (CLL) class
class CLL:
    def __init__(self):
        self.last = None  

    # Insert a new node at the beginning of the circular linked list
    def insert_first(self, value):
        n = node(value)  
        if self.last is None:  
            self.last = n  
            n.nex = n      
        else:
            n.nex = self.last.nex
            self.last.nex = n     

    # Insert a new node at the end of the circular linked list
    def insert_last(self, value):
        n = node(value, self.last.nex) 
        self.last.nex = n  
        self.last = n     

    # Insert a new node after the node with the given value
    def insert_ele(self, ele, value):
        n = node(value) 
        if self.last.value == ele:  
            n.nex = self.last.nex 
            self.last.nex = n     
            self.last = n        
        else:
            temp = self.last.nex  
            while temp.value != ele:  
                temp = temp.nex
            n.nex = temp.nex  
            temp.nex = n     

    # Delete the first node of the circular linked list
    def delete_first(self):
        if self.last is None:  
            return
        self.last.nex = self.last.nex.nex 

    # Delete the last node of the circular linked list
    def delete_last(self):
        if self.last is None:  
            return
        if self.last.nex == self.last:  
            self.last = None  
        else:
            temp = self.last.nex  
            while temp.nex != self.last:  
                temp = temp.nex
            temp.nex = self.last.nex  
            self.last = temp 

    # Delete a node with a specific value
    def delete(self, value):
        if self.last is None:  
            return
        if self.last.nex == self.last:  
            if self.last.value == value:  
                self.last = None  
        else:
            if self.last.nex.value == value:  
                self.delete_first()
            else:
                temp = self.last.nex 
                while temp != self.last:  
                    if temp.nex.value == value: 
                        temp.nex = temp.nex.nex  
                        break
                    temp = temp.nex

    # Search for a node with a specific value
    def search(self, value):
        if self.last is None:  
            print("List is empty")
            return None
        temp = self.last.nex 
        while True:
            if temp.value == value: 
                print(f"Node with value {value} found.")
                return temp  
            temp = temp.nex  
            if temp == self.last.nex:  
                break
        print(f"Node with value {value} not found.")
        return None  

    # Display the entire circular linked list
    def display(self):
        if self.last is None:  
            print("List is empty")
            return
        temp = self.last.nex  
        while True:
            print(temp.value, end=" ")  
            temp = temp.nex  
            if temp == self.last.nex:  
                break
        print()  

    # Iterator to traverse the circular linked list
    def __iter__(self):
        if self.last is None:  
            return ele(None)
        else:
            return ele(self.last.nex)  

# Iterator class for Circular Linked List
class ele:
    def __init__(self, start):
        self.curr = start  
        self.start = start  
        self.first_iteration = True  

    def __iter__(self):
        return self  

    def __next__(self):
        if self.curr is None:  
            raise StopIteration
        if self.curr == self.start and not self.first_iteration:  
            raise StopIteration
        else:
            self.first_iteration = False  

        data = self.curr.value  
        self.curr = self.curr.nex  
        return data

# Test code
e = CLL() 

# Insert at the beginning
e.insert_first(11)
e.display()  
print("---insert first")

# Insert at the end
e.insert_last(23)
e.insert_last(5)
e.insert_last(8)
e.display()  
print("---insert last")

# Insert after a specific node
e.insert_first(17)
e.display()  
print("---insert first")

e.insert_ele(5, 3)
e.display()  
print("---insert after 5")

# Delete the first element
e.delete_first()
e.display()  
print("---delete first")

# Delete the last element
e.delete_last()
e.display()  
print("---delete last")

# Delete a specific element
e.delete(23)
e.display() 
print("---delete 23")

# Search for an element in the list
e.search(3)  
e.search(10) 

# Iterate over the Circular Linked List and print elements
for l in e:
    print(l, end=" ") 
