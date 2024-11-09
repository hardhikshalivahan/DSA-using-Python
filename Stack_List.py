# Implementing a Stack in Python with Basic Operations: Push, Pop, Peek, and Size

# Stack implementation using a list
class stack:
    def __init__(self):
        # Initialize an empty list to hold stack elements
        self.l=[]

    def is_empty(self):
        # Check if the stack is empty
        return len(self.l)==0
    
    def push(self,value):
        # Add an element to the top of the stack
        self.l.append(value)

    def pop(self):
        # Remove and return the top element from the stack
        if not self.is_empty():
            return self.l.pop()
        else:
            raise IndexError("list is empty")
        
    def peek(self):
        # Return the top element without removing it
        if not self.is_empty():
            return self.l[-1]
        else:
            raise IndexError("list is empty")
        
    def size(self):
        # Return the number of elements in the stack
        return len(self.l)
    
# Example usage
h=stack()
h.push(12)
h.push(88)
h.push(44)
h.push(85)

print("size is: ",h.size())
print("pop element is: ",h.pop())
print("Top element is: ",h.peek())