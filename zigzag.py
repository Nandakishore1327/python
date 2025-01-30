class node():
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev=None

class link():
    def __init__(self):
        self.head = None
        self.temp = None

    def create(self, data):
        if self.head == None:
            self.head = node(data)
            self.head.prev = None
            self.head.next = None
            self.temp = self.head
            self.prev = self.head
        else:
            self.temp.next = node(data)
            self.temp = self.temp.next
            self.temp.prev = self.prev
            self.prev = self.temp

    def rear(self,obj):
        obj.tail=obj.temp
        obj.temp=obj.head
        self.head=obj.head
        self.temp=obj.temp
        while obj.temp !=obj.tail:
            self.temp.next=obj.tail
            self.temp=self.temp.next
            obj.temp=obj.temp.next
            obj.tail=obj.tail.prev
    def display(self):
        self.temp=self.head
        while self.temp!=None:
            print(self.temp.data)
            self.temp=self.temp.next


obj=link()
obj1=link()
obj.create(1)
obj.create(2)
obj.create(3)
obj.create(4)
obj1=link()
obj1.rear(obj)
obj1.display()