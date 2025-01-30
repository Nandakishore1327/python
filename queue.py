class node():
    def __init__(self,data):
        self.data=data
        self.next=None
class link():
    def __init__(self,max):
        self.front=None
        self.rear=None
        self.size=0
        self.max = max
    def enqueue(self,data):
        if self.size==self.max:
            print('Queue over flow')
        else:
            Node = node(data)
            if self.front == None:
                self.front = Node
                self.rear = self.front
            else:
                self.rear.next = Node
                self.rear = self.rear.next
            self.size += 1
    def dequeue(self):
        if self.front ==None:
            print('queue under flow')
        else:
            temp=self.front
            self.front=self.front.next
    def first(self):
        if self.front==None:
            print('queue under flow')
        else:
            print(self.front.data)
    def display(self):
        if self.front==None:
            print("queue under flow")
        else:
            self.rear = self.front
            while self.rear != None:
                print(self.rear.data, end=" ")
                self.rear = self.rear.next
            print("")
n=int(input())
queue=link(n)
queue.enqueue(10)
queue.enqueue(20)
queue.display()
queue.first()
queue.dequeue()
queue.display()
queue.dequeue()
queue.display()