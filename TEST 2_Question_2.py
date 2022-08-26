# DEQUEUE :
## Read input as specified in the question.
## Print output as specified in the question.

class Node :
    def __init__(self,data):
        self.data = data
        self.next = None

class Dequeue :
    def __init__(self):
        self.size = 0
        self.head = None
        self.last = None

    def insertFront(self,data):
        val = Node(data)
        if self.head is None :
            self.head = val
            self.last = val
        else:
            val.next = self.head
            self.head = val

    def insertRear(self,data):
        val = Node(data)
        if self.head is None:
            self.head = val
        else:
            self.last.next = val
            self.last = val

    def deleteRear(self):
        if self.head is None:
            print(-1)
        else:
            curr = self.head
            while curr.next.next is not None:
                prev = curr
                curr = curr.next
            prev.next = None
            self.last = prev

    def deleteFront(self):
        if self.head is None:
            print(-1)
        else:
            self.head = self.head.next

    def getFront(self):
        if self.head is None:
            return -1
        else:
            return self.head.data

    def getRear(self):
        if self.head is None:
            return -1
        else:
            return self.last.data

arr = [int(ele) for ele in input().split()]
d = Dequeue()
i = 0
while i < len(arr)-1 :
    if arr[i] == 1:
        d.insertFront(arr[i+1])
        i+=2
    elif arr[i] == 2:
        d.insertRear(arr[i+1])
        i+=2
    elif arr[i] == 3:
        d.deleteFront()
        i+=1
    elif arr[i] == 4:
        d.deleteRear()
        i+=1
    elif arr[i] == 5:
        print(d.getFront())
        i+=1
    elif arr[i] == 6:
        print(d.getRear())
        i+=1