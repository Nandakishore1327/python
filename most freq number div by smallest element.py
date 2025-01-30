class node():
    def __init__(self,data):
        self.data=data
        self.next=None
class link():
    def __init__(self):
        self.head=None
        self.temp=None
    def create(self,data):
        if self.head==None:
            self.head=node(data)
            self.temp=self.head
        else:
            self.temp.next=node(data)
            self.temp=self.temp.next
    def display(self):
        self.temp=self.head
        while self.temp.next !=None:
            print(self.temp.data,end=" ")
            self.temp=self.temp.next
        print(self.temp.data)
    def small(self):
        self.temp=self.head
        c=99
        while self.temp!=None:
            if self.temp.data<c:
                c=self.temp.data
            self.temp=self.temp.next
        return c
    def freq_count(self):
        self.temp=self.head
        res=0
        data=0
        while self.temp!=None:
            self.temp1=self.temp.next
            c=1
            while self.temp1!=None:
                if self.temp.data==self.temp1.data:
                    c+=1
                self.temp1=self.temp1.next
            if c>res:
                res=c
                data=self.temp.data
            self.temp=self.temp.next
        print(data)
        return data
obj=link()
l=int(input())
for i in range(l):
    obj.create(int(input("Enter the element: ")))
obj.display()
s=obj.small()
data=obj.freq_count()
if data%s==0:
    print("True")
else:
    print("False")