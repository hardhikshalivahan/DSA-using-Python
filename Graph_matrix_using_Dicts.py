# Implementation of Graph in dict

class graph:
    def __init__(self,no_vetices):
        self.no_vetices=no_vetices
        self.dict={v:[] for v in range(no_vetices)}

    def add(self,u,v,weight=1):
        if 0<=u<self.no_vetices and 0<=v<self.no_vetices:
            if not any(n==v for n,_ in self.dict[u]):
                self.dict[u].append((v,weight))
                self.dict[v].append((u,weight))

    def delete(self,u,v):
        if 0<=u<self.no_vetices and 0<=v<self.no_vetices:
            self.dict[u]=[(i,w) for i,w in self.dict[u] if i!=v]
            self.dict[v]=[(i,w) for i,w in self.dict[v] if i!=v]
        else:
            print("Invalid Index")

    def has(self,u,v):
        if 0<=u<self.no_vetices and 0<=v<self.no_vetices:
            return any(i==v for i,w in self.dict[u])
        else:
            return "Invalid Index"

    def display(self):
        for i,j in self.dict.items():
            print(i," : ",j)


l=graph(5)
l.add(0,1)
l.add(1,2)
l.add(2,3)
l.add(3,4)
l.add(5,0)

l.display()
