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

    def middle(self,mid):
        self.temp=self.head
        l=0
        while l<mid:
            self.temp = self.temp.next
            l+=1
        print(self.temp.data)


val = [int(x) for x in input().split()]
obj=link()
for i in range(len(val)):
    obj.create(val[i])
mid=len(val)//2
obj.middle(mid)