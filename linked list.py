class node():3+
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
        # print(self.temp.data)
    def display(self):
        self.temp=self.head
        while self.temp.next !=None:
            print(self.temp.data,end=" ")
            self.temp=self.temp.next
        print(self.temp.data)
    def delete_end(self):
        if self.head==None:
            print( "list is empty")
        else:
            self.temp = self.head
            self.prev = self.head
            while self.temp.next != None:
                self.prev = self.temp
                self.temp = self.temp.next
            self.prev.next = None
    def delete_front(self):
        if self.head==None:
            print( "list is empty")
        else:
            self.temp = self.head
            self.head = self.head.next
    def specdelete(self,n):
        if self.head==None:
            print( "list is empty")
        else:
            c = 0
            self.temp = self.head
            self.prev = self.head
            while c < n:
                self.prev = self.temp
                self.temp = self.temp.next
                c += 1
            self.prev.next = self.temp.next
    def insert_start(self,data):
        Node = node(data)
        if self.head==None:
            self.head=Node
            self.head.next=None
        else:
            self.temp = self.head
            self.head = Node
            self.head.next = self.temp
    def insert_pos(self,data,pos):
        Node = node(data)
        if self.head == None:
            self.head = Node
            self.head.next = None
        else:
            c = 0
            self.temp = self.head
            self.prev = self.head
            while c < pos:
                self.prev = self.temp
                self.temp = self.temp.next
                c += 1
            self.prev.next = Node
            Node.next = self.temp
    def insert_end(self,data):
        self.temp.next=node(data)
    def count(self):
        count=0
        if self.head==None:
            print(count)
        else:
            self.temp = self.head
            while self.temp.next != None:
                self.temp = self.temp.next
                count+=1

            print(count+1)
    def search(self,element):
         self.temp = self.head
         if self.head==None:
             print("LIST is empty")
         else:
             i=1
             flag=0
             while self.temp.next!=None:
                 if self.temp.data==element:
                     print("element is found at:",i)
                     flag = 1
                     break
                 else:
                     i+=1
                     self.temp=self.temp.next
             if flag==0:
                 print("element not found")

    def rev(self, l, r):
        if l == r:
            return self.head
        else:
            i = 1
            temp = self.head
            start, end = None, None
            prev = None
            while temp and i < r:
                if i == l:
                    start = temp
                if i == r:
                    end = temp
                prev = temp
                temp = temp.next
                i += 1

            if not start or not end:
                return self.head

            start.data, end.data = end.data, start.data
            return self.rev(start.next, prev)

    def reverse(self, head):
        if not head:
            return None
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

    def isPalindrome(self, head) :
        if not head:
            return True

        # Find the middle of the list
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half of the list
        second_half = self.reverse(slow)
        while second_half:
            if self.head.data != second_half.data:
                return False
            self.head = self.head.next
            second_half = second_half.next
        return True


obj=link()
obj.create(1)
obj.create(2)
obj.create(2)
obj.create(1)
# obj.create(5)
# obj.create(6)
# r=obj.rev(2,4)
obj.display()
print(obj.isPalindrome(1))

obj.display()

# print("1.Create")
# print("2.Delete at front")
# print("3.Delete at end")
# print("4.Delete at specific pos")
# print("5.Insert at front")
# print("6.Insert at end")
# print("7.Insert at specific pos")
# print("8.Count")
# print("9.search")
# print("10. Display")
# a='yes'
# while a=='yes':
#     choice = int(input("Enter your choice:"))
#     if choice!=0:
#         if choice==1:
#             element = int(input("Enter the element:"))
#             obj.create(element)
#         elif choice==2:
#             obj.delete_front()
#         elif choice==3:
#             obj.delete_end()
#         elif choice==4:
#             pos=int(input("Enter the position"))
#             obj.specdelete(pos)
#         elif choice==5:
#             element=int(input("Enter the element:"))
#             obj.insert_start(element)
#         elif choice==6:
#             element = int(input("Enter the element:"))
#             obj.insert_end(element)
#         elif choice==7:
#             element = int(input("Enter the element:"))
#             pos=int(input("Enter the position"))
#             obj.insert_pos(element,pos)
#         elif choice==8:
#             obj.count()
#         elif choice==9:
#             element = int(input("Enter the element to be searched:"))
#             obj.search(element)
#         elif choice==10:
#             obj.display()
#     a=input("Do you want to continue(yes/no):")


# obj.delete_end()
# obj.create(10)
# obj.create(20)
# obj.create(30)
# obj.create(40)
# print("Before delete")
# obj.display()
# print("Delete last element")
# obj.delete_end()
# obj.display()
# print("Delete first element")
# obj.delete_front()
# obj.display()
# print("After delete")
# obj.specdelete(1)
# obj.display()
# print("After inserting at front")
# obj.insert_start(5)
# obj.display()
# print("After inserting at pos")
# obj.insert_pos(11,1)
# obj.display()
# obj.count()
# obj.search(20)






# class node:
#     def __init__(self,data):
#         self.data=data
#         self.left=None
#         self.right=None
#
# class bst:
#     def __init__(self):
#         self.root=None
#
#     def create(self,root,data):
#         if not root:
#             return node(data)
#         elif root.data > data:
#             root.left = self.create(root.left,data)
#         else:
#             root.right=self.create(root.right,data)
#         return root
#
#
# mylist=list(map(int,input().split()))
# b=bst()
# for i in mylist:
#     b.root=b.create(b.root,i)
