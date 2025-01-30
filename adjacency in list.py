class graph:
    def __init__(self,size):
        self.adjmat={}
        for i in range(size):
            self.adjmat[i]=[]

    def add(self,v1,v2):
        self.adjmat[v1].append(v2)
        self.adjmat[v2].append(v1)
    def display(self):
        for key , val in self.adjmat.items():
            print(f'{key}',end="")
            for i in range(len(val)):
                print(f'->{val[i]}',end="")
            print()
    def bfs(self,src=None):
        self.visited=[]
        self.queue=[src]
        while self.queue:
            ele=self.queue.pop(0)
            print(ele,end=" ")
            self.visited.append(ele)
            for i in self.adjmat[ele]:
                if i  not in self.queue and i not in self.visited:
                    self.queue.append(i)
        print(self.queue)
        print(self.visited)
    def bfsrec(self,src=None,queue=None,visited=None):
        if queue is None:
            queue=[src]
        if visited is None:
            visited=[]
        if not queue:
            print(visited)
            return
        ele=queue.pop(0)
        visited.append(ele)
        for i in self.adjmat[ele]:
            if i not in queue and i not in visited:
                queue.append(i)
        self.bfsrec(src=None,queue=queue,visited=visited)
    def dfs(self,src=None):
        self.visited=[]
        self.stack=[src]
        while self.stack:
            ele=self.stack.pop()
            print(ele,end=" ")
            self.visited.append(ele)
            for i in self.adjmat[ele]:
                if i not in self.stack and i not in self.visited:
                    self.stack.append(i)
        print(self.stack)
        print(self.visited)

    def dfsrec(self, src=None, stack=None, visited=None):
        if stack is None:
            stack = [src]
        if visited is None:
            visited = []
        if not stack:
            print(visited)
            return
        ele = stack.pop()
        visited.append(ele)
        for i in self.adjmat[ele]:
            if i not in stack and i not in visited:
                stack.append(i)
        self.dfsrec(src=None, stack=stack, visited=visited)

size=int(input("Enter the no of vertices: "))
g=graph(size)
# edge=int(input("Enter the no of edges: "))
# for i in range(edge):
#     n,m=map(int,input("Enter v1 and v2:").split())
#     g.add(n,m)
g.add(0,1)
g.add(0,2)
g.add(0,4)
g.add(1,4)
g.add(2,3)
g.add(3,4)
g.display()
g.bfs(0)
g.dfsrec(0)
# g.bfs(0)
# g.dfs(0)

