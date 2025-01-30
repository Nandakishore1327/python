class node():
    def __init__(self, data):
        self.data = data
        self.next = None

class link():
    def __init__(self):
        self.head = None
        self.temp = None

    def create(self, data):
        if self.head == None:
            self.head = node(data)
            self.temp = self.head
        else:
            self.temp.next = node(data)
            self.temp = self.temp.next

    def zigzag(self,l1,l2):
        res = link()
        current1 = l1.head
        current2 = l2.head
        while current1 is not None and current2 is not None:
            res.create(current1.data)
            res.create(current2.data)
            current1 = current1.next
            current2 = current2.next
        while current1 is not None:
            res.create(current1.data)
            current1 = current1.next
        while current2 is not None:
            res.create(current2.data)
            current2 = current2.next
        current = res.head
        return current
        # while current is not None:
        #     print(current.data, end=" -> " if current.next is not None else "")
        #     current = current.next
    def display(self):
        self.temp=self.head
        while self.temp.next !=None:
            print(self.temp.data,end=" ")
            self.temp=self.temp.next
        print(self.temp.data)
obj=link()
obj1=link()
obj.create(1)
obj.create(3)
obj.create(5)
obj.create(7)
obj1.create(2)
obj1.create(4)
obj1.create(6)
obj1.create(8)
obj.display()
obj1.display()
obj2=link()
re=obj2.zigzag(obj,obj1)
while re:
    print(re.data,end=" ")
    re=re.next
