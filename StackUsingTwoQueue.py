
from sys import stdin


class Stack :
    def __init__(self):
        self.__data1=[]
        self.__data2=[]
        self.__front1 = 0
        self.__front2 = 0

    def getSize(self) :
        if self.isEmpty():
            return -1
        else:
            return len(self.__data1)

    def isEmpty(self) :
        return self.getSize() == 0

    def push(self, data) :
        self.__data1.append(data)


    def pop(self) :
        if self.isEmpty():
            return -1
        else:
            while len(self.__data1)!=1:
                self.__data2.append(self.__data1.pop(self.__front1))
            
            data = self.__data1.pop(self.__front1)
        
            while len(self.__data2)!=0:
                self.__data1.append(self.__data2.pop(self.__front2))

        return data

    def top(self) :
        if self.isEmpty():
            return -1
        else:
            return self.__data1[0]

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