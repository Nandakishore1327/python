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
        while self.temp !=None:
            print(self.temp.data,end=" ")
            self.temp=self.temp.next
        print("")
    def reverse(self):
        curr=self.head
        prev=None
        next=None
        while curr!=None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head=prev
    def spilt(self,eve,odd):
        c=1
        self.temp=self.head
        while self.temp!=None:
            if c%2!=0:
                odd.create(self.temp.data)
            else:
                eve.create(self.temp.data)
            self.temp=self.temp.next
            c+=1
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
        while current!=None:
            print(current.data,end=" ")
            current=current.next
obj=link()
m=int(input())
for i in range(m):
    obj.create(int(input("Enter the element")))
obj.display()
eve=link()
odd=link()
obj.spilt(eve,odd)
eve.display()
odd.display()
eve.reverse()
eve.display()
obj.zigzag(odd,eve)
