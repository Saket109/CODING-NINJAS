
from sys import stdin

#Following is the structure of the node class for a Singly Linked List
class Node :

    def __init__(self, data) :
        self.data = data
        self.next = None


class Stack :
    def __init__(self):
        self.__data = []
        

    '''----------------- Public Functions of Stack -----------------'''

    def getSize(self) :
        return len(self.__data)

    def isEmpty(self) :
        return self.getSize(self.__data) == 0

    def push(self, data) :
        self.__data.append(data)

    def pop(self) :
        if self.isEmpty():
            return -1
        return self.__data.pop()
            
    def top(self) :
        if self.isEmpty():
            return -1
        return self.__data[len(self.__data)-1]
    
#main
q = int(stdin.readline().strip())

stack = Stack()

while q > 0 :

    inputs = stdin.readline().strip().split(" ")
    choice = int(inputs[0])

    if choice == 1 :
        data = int(inputs[1])
        stack.push(data)

    elif choice == 2 :
        print(stack.pop())

    elif choice == 3 :
        print(stack.top())

    elif choice == 4 : 
        print(stack.getSize())

    else :
        if stack.isEmpty() :
            print("true")
        else :
            print("false")

    q -= 1