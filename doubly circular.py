class node():
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class link():
    def __init__(self):
        self.head=None
        self.temp=None
        self.prev=None
    def create(self,data):
        if self.head==None:
            self.head=node(data)
            self.head.prev=None
            self.head.next=None
            self.temp=self.head
            self.prev= self.head
        else:
            self.temp.next=node(data)
            self.temp=self.temp.next
            self.temp.prev=self.prev
            self.prev=self.temp
        self.temp.next=self.head
        self.head.prev=self.temp
    def display(self):
        self.temp=self.head
        while self.temp.next !=self.head:
            print(self.temp.data,end=" ")
            self.temp=self.temp.next
        print(self.temp.data)
obj=link()
obj.create(10)
obj.create(20)
obj.create(30)
obj.create(40)
obj.display()
