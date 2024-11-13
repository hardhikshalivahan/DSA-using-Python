#Deque implementation using Double Linked List

class node:
    def __init__(self,prev=None,value=None,nex=None):
        self.prev=prev
        self.value=value
        self.nex=nex
        
class Deque:
    def __init__(self,front=None,rear=None):
        self.front=front
        self.rear=rear
        self.count=0
        
    def insert_start(self,value):
        n=node(value=value)
        if self.count==0:
            self.front=n
            self.rear=self.front
        else:
            self.front.prev=n
            n.nex=self.front
            self.front=n
        self.count+=1
        
    def insert_end(self,value):
        n=node(value=value)
        if self.count==0:
            self.rear=n
            self.front=self.rear
        else:
            self.rear.nex=n
            n.prev=self.rear
            self.rear=n
        self.count+=1
    def delete_start(self):
        val=self.front.value
        self.count-=1
        if self.count==0:
            return ("There are no elements in the Deque")
        else:
            self.front=self.front.nex
            self.front.prev=None
            return val
            
    def delete_end(self):
        val=self.rear.value
        self.count-=1
        if self.count==0:
            return ("There are no elements in the Deque")
        else:
            self.rear=self.rear.prev
            self.rear.nex=None
            return val
    def size(self):
        return self.count
    
    def get_front(self):
        try:
            if self.count==0:
                raise IndexError("No elements in the Deque")
            else:
                return self.front.value
        except IndexError as e:
            print(e.args[0])
            
    def get_rear(self):
        try:
            if self.count==0:
                raise IndexError("No elements in the Deque")
            else:
                return self.rear.value
        except IndexError as e:
            print(e.args[0])

# Example usage

h=Deque()
print("first element is: ",h.get_front())
print("last element is: ",h.get_rear())
print("Total elements: ",h.size())
print()
h.insert_start(10)
h.insert_start(20)
h.insert_end(30)
h.insert_end(40)
print("first element is: ",h.get_front())
print("last element is: ",h.get_rear())
print("Total elements: ",h.size())
print()
print("Deleted element is: ",h.delete_start())
print("Deleted element is: ",h.delete_end())
print("first element is: ",h.get_front())
print("last element is: ",h.get_rear())
print("Total elements: ",h.size())