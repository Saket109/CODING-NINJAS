# FOR IMPROVING TIME COMPLEXITY THEN WE WILL USE REHASHING MEANS INCREASE THE SIZE OF
    # BUCKET SIZE TO MAINTAIN N/B < 0.7

class mapNode:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None

class map:
    def __init__(self):
        self.bucketsize = 10
        self.buckets = [None for i in range(self.bucketsize)]
        self.count = 0

    def size(self):
        return self.count
    
    def getindex(self,hc):
        index = abs(hc)%(self.bucketsize)
        return index

    def rehash(self):
        temp = self.buckets
        self.buckets = [None for i in range(2*self.bucketsize)]
        self.bucketsize = 2*self.bucketsize
        self.count = 0
        for head in temp:
            while head is not None:
                self.insert(head.key,head.value)
                head = head.next

    def loadfactor(self):
        return self.count/self.bucketsize

    def insert(self,key,value):

        hc = hash(key)
        index = self.getindex(hc)
        head = self.buckets[index]
        while head is not None:
            if head.key == key:
                head.value = value
                return
            head = head.next

        head = self.buckets[index]
        newnode = mapNode(key,value)
        newnode.next = head
        self.buckets[index] = newnode
        self.count += 1
        loadfactor = self.count/self.bucketsize
        if loadfactor>=0.7:
            self.rehash()      

    def search(self,key):
        hc = hash(key)
        index = self.getindex(hc)
        head = self.buckets[index]
        while head is not None:
            if head.key == key:
                return head.value
            head = head.next

        return -1

    def delete(self,key):
        hc = hash(key)
        index = self.getindex(hc)
        head = self.buckets[index]
        if head.key == key:
            head = head.next
            self.buckets[index] = head
            self.count -= 1
            return
        while head is not None:
            if head.next is not None and head.next.key == key:
                head.next = head.next.next
                self.count-=1
                return
            head = head.next
                

                


m = map()

for i in range(10):
    m.insert('abc'+str(i),i+1)
    print(m.loadfactor())
    
for i in range(10):
    print('abc'+str(i)+':',m.search('abc'+str(i)))
# m.insert("saket",10)
# print(m.size())
# m.insert("kohli",18)
# print(m.size())
# m.insert("saket",16)
# print(m.size())
# print(m.search("saket"))
# m.delete("saket")
# print(m.size())
# print(m.search("saket"))
