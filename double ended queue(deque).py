class node():
    def __init__(self):
        self.front = -1
        self.rear = -1

    def insert_at_front(self, l):
        ele = int(input("Enter the element:"))
        l.insert(0, ele)

    def insert_at_rear(self, l):
        ele = int(input("Enter the element:"))
        l.append(ele)
        self.rear = ele

    def delete_at_front(self, l):
        self.front = l[1]
        l.pop(0)

    def delete_at_rear(self, l):
        self.rear = len(l) - 1
        l.pop()

l = [1, 2, 3, 4]
o = node()
o.insert_at_front(l)
o.insert_at_rear(l)
o.delete_at_rear(l)
o.delete_at_front(l)
print(l)
