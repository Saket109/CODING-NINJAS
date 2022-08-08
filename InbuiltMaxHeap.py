import heapq

li = [4,7,6,90,87,34,45,66]
# TO CREATE THE MAX HEAP WE WILL USE THE PRIVATE FUNCTION _HEAPIFY_MAX()
heapq._heapify_max(li)
print(li)

# TO GET THE MAX ELEMENT WE WILL USE THE FUNCTION _HEAPPOP_MAX(LIST)
print(heapq._heappop_max(li))
print(li)

# TO REPLACE THE MAX ELEMENT WITH ELE THEN USE THE FUNCTION _HEAPREPLACE_MAX(LIST,ELE)
print(heapq._heapreplace_max(li,58))
print(li)

# TO PUSH THE ELE IN THE MAX HEAP WE WILL USE THE FOLLOWING (FUNCTION USED --> _SIFTDOWN_MAX())
li.append(38)
heapq._siftdown_max(li,0,len(li)-1)
print(li)