class node():
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class link():
    def __init__(self):
        self.front=None
        self.rear=None

    def enqueue_at_rear(self,data):
        Node = node(data)
        if self.front == None:
            self.front = Node
            self.rear = self.front
        else:
            self.rear.next = Node
            Node.prev=self.rear
            self.rear = self.rear.next

    def dequeue_at_front(self):
        if self.front == None:
            print('queue under flow')
        elif self.front == self.rear:
            self.front=None
            self.rear=None
        else:
            self.front=self.front.next
            self.front.prev=None
            print(self.front.data)


    def enqueue_at_front(self,data):
        Node=node(data)
        if self.front==None:
            self.front=Node
            self.rear=self.front
        else:
            Node.next = self.front
            self.front.prev = Node
            self.front = Node

    def dequeue_at_rear(self):
        if self.front == None :
            print('queue under flow')
        elif self.front==self.rear:
            self.front=None
            self.rear=None
        else:
            self.rear=self.rear.prev
            self.rear.next=None
            print(self.rear.data)

    def display(self):
        temp=self.front
        while temp!=None :
            print(temp.data,end=" ")
            temp=temp.next
        print("")
o=link()
o.enqueue_at_rear(10)
o.enqueue_at_rear(20)
o.enqueue_at_rear(30)
o.enqueue_at_rear(40)
o.enqueue_at_rear(50)
o.display()
o.enqueue_at_front(5)
print("After enqueue at front")
o.display()
o.enqueue_at_rear(60)
print("After enqueue at rear")
o.display()
o.dequeue_at_rear()
print("After dequeue at rear")
o.display()
o.dequeue_at_front()
print("After dequeue at front")
o.display()



