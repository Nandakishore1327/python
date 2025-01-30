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
    def lrotate(self,k):
        self.temp=self.head
        # print(self.temp.data)
        i=1
        while i<k:
            i+=1
            self.temp=self.temp.next
        self.tail.next=self.head
        self.head=self.temp.next
        self.temp.next=None
obj=link()
li=list(map(int,input().split()))
for i in range(li[0]):
    obj.create(int(input("Enter the element")))
obj.display()
obj.lrotate(li[1])
obj.display()