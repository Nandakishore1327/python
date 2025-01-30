class graph:
    def __init__(self,size):
        self.adjmat=[]
        for i in range(size):
            self.adjmat.append([0 for i in range(size)])
        self.size=size
    def addedge(self,v1,v2):
        if v1==v2:
            print("Same edge")
        self.adjmat[v1][v2]=1
        self.adjmat[v2][v1]=1
    def display(self):
        for row in self.adjmat:
            for val in row:
                print(val,end=" ")
            print()
g=graph(5)
g.addedge(0,1)
g.addedge(0,2)
g.addedge(0,4)
g.addedge(1,4)
g.addedge(2,3)
g.addedge(3,4)
g.display()