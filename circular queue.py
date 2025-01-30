class queue():
    def __init__(self,size=10):
        self.front=-1
        self.rear=-1
        self.q=[]*size
        self.size=size
    def dequeue(self):
        if self.front==-1 and self.rear==-1:
            print("QUEUE IS EMPTY")
        elif self.front==self.rear:
            self.front=self.rear=-1
        else:
            self.front=(self.front+1)%self.size
            print(self.front)

    def enqueue(self,l):
        self.rear=(self.rear+1)%self.size
        if self.rear==self.front:
            print("QUEUE IS Full")
        else:
            print("hi")
o=queue()
o.dequeue()
o.enqueue()