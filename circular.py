class node():
    def __init__(self,data):
        self.data=data
        self.next=None
class link():
    def __init__(self):
        self.head=None
        self.temp=None
        self.tail=None
    def create(self,data):
        if self.head==None:
            self.head=node(data)
            self.tail=self.head
        else:
            self.tail.next=node(data)
            self.tail=self.tail.next
        self.tail.next=self.head

    def insert_start(self,data):
        Node = node(data)
        self.temp = self.head
        if self.head==None:
            self.head=Node

        else:
            self.head = Node
            self.head.next = self.temp
        self.tail.next = self.headq

    def display(self):
        self.temp = self.head
        while self.temp.next != self.head:
            print(self.temp.data, end=" ")
            self.temp = self.temp.next
        print(self.temp.data)
obj=link()
obj.create(10)
obj.create(20)
obj.create(30)
obj.create(40)
obj.insert_start(5)
obj.display()