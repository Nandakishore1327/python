class Node:
    def __init__(self, data):
        self.previous = None
        self.data = data
        self.next = None


class Linkedlist:
    def __init__(self):
        self.delete = None
        self.head = None
        self.temp = None
        self.tail = None

    def insertbeg(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            self.tail = newnode
            self.temp = self.head
        else:
            self.head.previous = newnode
            newnode.next = self.head
            self.head = newnode
        print("LIST AFTER INSERTION")
        self.print()

    def insertmiddle(self, data, pos):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            self.tail = newnode
            self.temp = self.head
        else:
            self.temp = self.head
            count = 1
            while count < pos - 1:
                print(self.temp.data)
                self.temp = self.temp.next
                count += 1
            newnode.previous = self.temp
            newnode.next = self.temp.next
            self.temp.next = newnode
            self.temp = newnode
        print("LIST AFTER INSERTION")
        self.print()

    def insertend(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            self.tail = newnode
            self.temp = self.head
        else:
            self.tail.next = newnode
            self.tail = newnode
            newnode.previous = self.tail
            self.tail.next = None
        print("LIST AFTER INSERTION")
        self.print()

    def deletebeg(self):
        self.delete = self.head
        self.head= self.head.next
        self.head.previous = None
        del self.delete
        print("LIST AFTER DELETION")
        self.print()

    def deletemiddle(self,  pos):
        length = self.length()
        print("Length: ", length)
        if length < pos:
            return "Position out of range"
        if length == 0:
            return "EMPTY LINKED LIST"
        elif length == 1:
            self.head = None
        elif length == 2:
            self.delete = self.head.next
            self.head.next= None
            del self.delete
        else:
            count = 1
            self.temp = self.head
            while count< pos-1:
                self.temp = self.temp.next
                count += 1
            self.delete = self.temp.next
            self.temp.next = self.temp.next.next
            self.temp = self.temp.next.next
            self.delete.next= None
            del self.delete
        print("LIST AFTER DELETION")
        self.print()

    def deleteend(self):
        print("prev",self.tail.previous.data)
        self.temp = self.head
        while self.temp.next.next:
            self.temp = self.temp.next
        self.delete = self.temp.next
        self.temp.next = None
        self.delete.previous = None
        del self.delete
        print("LIST AFTER DELETION")
        self.print()

    def length(self):
        self.temp = self.head
        count = 0
        while self.temp:
            self.temp = self.temp.next
            count+= 1
        return count

    def print(self):
        if self.head is None:
            return "LINKED LIST IS EMPTY"
        else:
            self.temp = self.head
            while self.temp:
                print(self.temp.data, end=" ")
                self.temp = self.temp.next


ll = Linkedlist()
a = [1,2,3,4,5]
for i in a:
    ll.insertend(i)
print("DOUBLY LINKED LIST IMPLEMENTATION")
while 1:
    print("""
1. Insertion at beg
2. Insertion at middle
3. Insertion at end
4. Delete at start
5. Delete at middle
6. Delete at end
7. Display
8. Exit
""")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        num = int(input("Enter data: "))
        ll.insertbeg(num)
    elif ch == 2:
        num = int(input("Enter data: "))
        x = int(input("Enter position to insert: "))
        ll.insertmiddle(num, x)
    elif ch == 3:
        num = int(input("Enter data: "))
        ll.insertend(num)
    elif ch == 4:
        ll.deletebeg()
    elif ch == 5:
        x = int(input("Enter position to delete: "))
        ll.deletemiddle(x)
    elif ch == 6:
        ll.deleteend()
    elif ch == 7:
        print("PRINTING LINKED LIST ELEMENTS")
        ll.print()
    elif ch == 8:
        exit()
    else:
        print("Invalid input")
    print()
