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
            self.temp=self.head
        else:
            self.temp.next=node(data)
            self.temp=self.temp.next
        self.tail=self.temp
    def display(self):
        self.temp=self.head
        while self.temp.next !=None:
            print(self.temp.data,end=" ")
            self.temp=self.temp.next
        print(self.temp.data)
    def rotate(self,k):
        if k>1:
            c = 1
            while k:
                temp = self.head
                while temp.next != None:
                    temp = temp.next
                    if c == k:
                        stop = temp
                    c += 1
                    tail = temp
                k -= 1
            dum = stop.next
            stop.next = None
            tail.next = self.head
            self.head = dum

obj=link()
# li=list(map(int,input().split()))
# for i in range(li[0]):
#     obj.create(int(input("Enter the element")))
obj.create(1)
obj.create(2)
obj.create(3)
obj.create(4)
obj.create(5)
obj.display()
obj.rotate(1)
obj.display()