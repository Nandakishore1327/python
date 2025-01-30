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
    def reverse(self,head):
        if head is None or head.next is None:
            return head
        prev = None
        next = None
        curr = head
        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        head = prev
        return head
    def add(self,first,second):
        cur1=self.reverse(first.head)
        cur2=self.reverse(second.head)
        sum=0
        carry=0
        res=None
        prev=None
        while cur1 is not None or cur2 is not None:
            sum= carry +(cur1.data if cur1 else 0)+(cur2.data if cur2 else 0)

            carry = (1 if sum>=10 else 0)
            if sum>=10:
                sum=sum%10

            temp=node(sum)
            if res is None:
                res=temp
            else:
                prev.next=temp
            prev=temp
            if cur1:
                cur1= cur1.next
            if cur2 :
                cur2 =cur2.next
        ans=self.reverse(res)
        while ans is not None:
            print(ans.data,"->",end=" ")
            ans=ans.next
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
obj2.add(obj,obj1)

