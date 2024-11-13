#Implimentation of Priority Queue using Linked List

class node:
    def __init__(self,prio=None,value=None,nex=None):
        self.prio=prio
        self.value=value
        self.nex=nex

class PriorityQueue:
    def __init__(self,start=None):
        self.start=start
        self.count=0
        
    def push(self,prio,value):
        n=node(prio=prio,value=value)
        self.count+=1
        if not self.start or self.start.prio>prio:
            n.nex=self.start
            self.start=n
        else:
            temp=self.start
            while temp.nex!=None and temp.nex.prio<prio:
                temp=temp.nex
            n.nex=temp.nex
            temp.nex=n

    def pop(self):
        c=self.start.value
        self.count-=1
        self.start=self.start.nex
        return c
    
    def size(self):
        return self.count
    
    def ele(self):
        temp=self.start
        while temp!=None:
            print(temp.value)
            temp=temp.nex


# Example usage
h=PriorityQueue()
print("size of the queue is: ",h.size())
h.push(10,11)
h.push(2,23)
h.push(1,3)
h.push(4,17)
h.ele()
print("size of the queue is: ",h.size())
print("popped element is: ",h.pop())
print("size of the queue is: ",h.size())