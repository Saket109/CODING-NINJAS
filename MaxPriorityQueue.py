
class priorityQueueNode:
    def __init__(self,value,priority):
        self.value = value
        self.priority = priority

class priorityQueue:
    def __init__(self):
        self.pq = []

    def size(self):
        return len(self.pq)

    def isEmpty(self):
        return self.size() == 0

    def __percolateDown(self):
        ans = self.pq[0].value
        self.pq[0],self.pq[self.size()-1] = self.pq[self.size()-1],self.pq[0]
        self.pq.pop()
        parentIndex = 0
        LchildIndex = 2*parentIndex+1
        RchildIndex = 2*parentIndex+2
        
        while LchildIndex < self.size():
            maxIndex = parentIndex
            if self.pq[maxIndex].priority < self.pq[LchildIndex].priority:
                maxIndex = LchildIndex
            if RchildIndex < self.size() and self.pq[maxIndex].priority < self.pq[RchildIndex].priority:
                maxIndex = RchildIndex
            if maxIndex == parentIndex:
                break
            self.pq[parentIndex],self.pq[maxIndex] = self.pq[maxIndex],self.pq[parentIndex]
            parentIndex = maxIndex
            LchildIndex = 2*parentIndex+1
            RchildIndex = 2*parentIndex+2

        return ans


    def getmax(self):
        ans = self.__percolateDown()
        return ans

    def __percolateUp(self):
        childIndex = self.size()-1
        while childIndex>0:
            parentIndex = (childIndex-1)//2
            if self.pq[parentIndex].priority < self.pq[childIndex].priority:
                self.pq[parentIndex],self.pq[childIndex] = self.pq[childIndex],self.pq[parentIndex]
                childIndex = parentIndex
            else:
                break

    def insert(self,value,priority):
        data = priorityQueueNode(value,priority)
        self.pq.append(data)
        self.__percolateUp()


m = priorityQueue()
m.insert("a",10)
m.insert("b",40)
m.insert("c",1)
m.insert("d",30)
for i in range(4):
    print(m.getmax())