class node():
    def __init__(self,data):
        self.data=data
        self.next=None
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
            self.rear = self.rear.next

    def dequeue_at_front(self):
        if self.front == None:
            print('queue under flow')
        elif self.front ==self.rear:
            self.front=None
            self.rear=None
        else:
            temp=self.front
            self.front=self.front.next
            temp=None

    def enqueue_at_front(self,data):
        Node=node(data)
        Node.next=self.front
        self.front=Node

    def dequeue_at_rear(self):
        if self.front == None:
            print('queue under flow')
        elif self.front==self.rear:
            self.front=None
            self.rear=None
        else:
            temp = self.front
            while temp.next != self.rear:
                temp = temp.next
            temp.next=None
            self.rear, temp = temp, self.rear
    def display(self):
        temp=self.front
        while temp!=None:
            print(temp.data,end=" ")
            temp=temp.next
        print("")
o=link()
o.enqueue_at_rear(10)
o.enqueue_at_rear(20)
o.enqueue_at_rear(30)
o.enqueue_at_rear(40)
o.enqueue_at_rear(50)
print("Before enqueue at front")
o.display()
o.enqueue_at_front(5)
print("After enqueue at front")
o.display()
print("Before enqueue at rear")
o.display()
o.enqueue_at_rear(60)
print("After enqueue at rear")
o.display()
print("Before dequeue at rear")
o.display()
o.dequeue_at_rear()
print("After dequeue at rear")
o.display()
print("Before dequeue at front")
o.display()
o.dequeue_at_front()
print("After dequeue at front")
o.display()



