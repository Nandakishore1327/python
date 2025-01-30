class node():
    def __init__(self,data):
        self.data=data
        self.next=None
class link():
    def __init__(self,max):
        self.head=None
        self.temp=None
        self.size=0
        self.max = max
    def push(self,data):
        if self.size==self.max:
            print('stack overflow')
        else:
            Node = node(data)
            if self.head == None:
                self.head = Node
            else:
                Node.next = self.head
                self.head = Node
            self.size+=1
    def pop(self):
        if self.head==None:
            print('Satck is empty')
        else:
            temp=self.head
            self.head=self.head.next
            temp=None
    def peek(self):
        if self.head==None:
            print('Stack is empty')
        else:
            print(self.head.data)
    def display(self):
        temp=self.head
        if self.head==None:
            print('Stack is empty')
        else:
            while temp !=None:
                print(temp.data,end=" ")
                temp=temp.next
            print("")

n=int(input())
stack=link(n)
stack.push(10)
stack.push(20)
stack.push(30)
stack.display()
# stack.pop()
# stack.display()
# stack.peek()
stack.push(40)
stack.display()
stack.push(50)
stack.display()


