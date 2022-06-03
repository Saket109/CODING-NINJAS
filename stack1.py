class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

class Stack:
    def __init__(self):
        self.__head = None
        self.__count = 0

    def push(self,item):
        newnode = Node(item)
        newnode.next = self.__head
        self.__head = newnode
        self.__count += 1

    def pop(self):
        if self.isEmpty():
            return -1
        data = self.__head.data
        self.__head = self.__head.next
        self.__count -= 1
        return data

    def top(self):
        if self.isEmpty():
            return -1
        return self.__head

    def size(self):
        return self.__count

    def isEmpty(self):
        return self.size() == 0

s = Stack()
s.push(20)
print(s.pop())
print(s.isEmpty())
s.push(29)
s.push(19)
while s.isEmpty() is False:
    print(s.pop())