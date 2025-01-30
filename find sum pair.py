class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class link:
    def __init__(self):
        self.head=None
        self.temp=None
    def create(self,data):
        Node=node(data)
        if self.head==None:
            self.head=Node
            self.temp=self.head
        else:
            self.temp.next=Node
            Node.prev=self.temp
            self.temp=Node
    def scount(self,n):
        temp=self.head
        while temp.next:
            prev=temp.next
            while prev:
                if temp.data+prev.data==n:
                    print(temp.data, prev.data)
                prev=prev.next
            temp=temp.next

obj=link()
for i in range(5):
    obj.create(int(input()))
n=int(input())
obj.scount(n)
