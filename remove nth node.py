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
    def removeele(self,n):
        pos = 0
        temp = self.head
        while pos < n and temp:
            temp = temp.next
            pos += 1
        # print(temp.data)
        # print(temp.next.data)
        temp.next = temp.next.next

obj=link()
# li=list(map(int,input().split()))
# for i in range(li[0]):
#     obj.create(int(input("Enter the element")))
# obj.display()
# obj.removeele(li[1])
obj.create(1)
obj.create(2)
obj.create(3)
obj.create(4)
obj.create(5)
obj.display()
obj.removeele(2)
obj.display()