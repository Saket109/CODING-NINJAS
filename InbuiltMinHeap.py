# there is a inbuitl function called heapq used for building the heap
import heapq
li = [4,5,6,2,3,90,47,59]
heapq.heapify(li)
print(li)

heapq.heappush(li,74)
print(li)

print(heapq.heappop(li))
print(heapq.heappop(li))
print(heapq.heappop(li))
print(heapq.heappop(li))

## Functions are : 
        # heapq.heapify(list)
        # heapq.heappop(list) --> return the min element
        # heapq.heappush(list,ele)  --> push the ele in the list and maintain the min heap
        # heapq.heapreplace(list,ele) --> return the min element and replace it with the ele and then maintain the min heap
            # We can think of heapreplace as the combination of heappush and heappop together.
