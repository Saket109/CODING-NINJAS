class Queue:
    def __init__(self):
        self.__data=[]
        self.__count=0
        self.__front=0

    def Enqueue(self,item):
        self.__data.append(item)
        self.__count+=1

    def Dequeue(self):
        if self.isEmpty():
            return -1
        else:
            data = self.__data[self.__front]
            self.__front+=1
            self.__count-=1
            return data

    def Size(self):
        return self.__count

    def Front(self):
        if self.isEmpty():
            return -1
        else:
            return self.__data[self.__front]

    def isEmpty(self):
        return self.Size == 0

q = Queue()
q.Enqueue(1)
q.Enqueue(2)
q.Enqueue(3)
print(q.Dequeue())
print(q.Dequeue())
print(q.Size())
q.Enqueue(10)
print(q.Front())