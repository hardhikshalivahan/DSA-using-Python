# Implementing a Queue in Python with Basic Operations: enqueue, dequeue, get_rear, get_front, and Size

class Node:
    def __init__(self, value=None, nex=None):
        self.value = value
        self.nex = nex

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.counts = 0
         
    def enqueue(self, value):
        new_node = Node(value=value)
        if self.front is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.nex = new_node
            self.rear = new_node
        self.counts += 1
        
    def dequeue(self):
        if self.counts == 0:
            print("The Queue is empty")
            return None
        val = self.front.value
        self.front = self.front.nex
        self.counts -= 1
        if self.front is None:  
            self.rear = None
        return val
    
    def size(self):
        return self.counts

    def get_rear(self):
        return self.rear.value if self.rear else None

    def get_front(self):
        return self.front.value if self.front else None

# Example usage
q = Queue()
q.enqueue(10)
q.enqueue(11)
q.enqueue(12)
print("Size of the queue is:", q.size())
print("Front value is:", q.get_front())
print("Rear value is:", q.get_rear())
print("Deleted element is:", q.dequeue())
print("Deleted element is:", q.dequeue())
print("Deleted element is:", q.dequeue())
print("Deleted element is:", q.dequeue())
