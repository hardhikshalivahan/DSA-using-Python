# Implementing a Stack in Python with Basic Operations: Push, Pop, Peek, and Size

# Define a Node class to represent each element in the stack
class Node:
    def __init__(self, value=None, nex=None):
        self.value = value
        self.nex = nex

# Define a Stack class to implement stack operations
class Stack:
    def __init__(self, start=None):
        self.start = start
        self.counts = 0

    # Check if the stack is empty
    def is_empty(self):
        return self.start is None

    # Add a new element to the top of the stack
    def push(self, value):
        n = Node(value, self.start)
        self.start = n
        self.counts += 1

    # Remove and return the top element from the stack
    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        else:
            value = self.start.value
            self.start = self.start.nex
            self.counts -= 1
            return value

    # Return the current size of the stack
    def size(self):
        return self.counts

    # Return the value of the top element without removing it
    def peek(self):
        if not self.is_empty():
            return self.start.value
        else:
            return "Stack is empty"

# Test the stack implementation
la = Stack() 
la.push(21)   
la.push(22)
la.push(23)
la.push(24)
la.push(25)

print("Popped element is:", la.pop())
print("Size of stack is:", la.size())
print("Last value is:", la.peek())