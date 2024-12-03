# Implementation of Graph Adjacency in Matrix

class graph:
    def __init__(self,no_vetices):
        self.no_vetices=no_vetices
        self.matrix=[[0]*no_vetices for i in range(no_vetices)]

    def add(self,u,v,weight=1):
        if 0<=u<self.no_vetices and 0<=v<self.no_vetices:
            self.matrix[u][v]=weight
            self.matrix[v][u]=weight

    def delete(self,u,v,weight=1):
        if 0<=u<self.no_vetices and 0<=v<self.no_vetices:
            self.matrix[u][v]=0
            self.matrix[v][u]=0

    def has_mat(self,u,v):
        if 0<=u<self.no_vetices and 0<=v<self.no_vetices:
            return self.matrix[u][v]!=0
        else:
            print("Invalid syntax")

    def display(self):
        for row in self.matrix:
            print(" ".join(map(str,row)))


l=graph(5)
l.add(1,3)
l.add(3,2)
l.add(0,3)
l.add(3,4)
l.add(2,1)
print(l.has_mat(4,3))
l.display()
l.delete(0,3)
print("After Deleting...")
l.display()
