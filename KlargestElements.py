import heapq
def kLargest(lst, k):
    heap = lst[:k]
    heapq.heapify(heap)
    for i in lst[k:]:
        if heap[0] < i:
            heapq.heapreplace(heap,i)
        
    return heap

# Main Code
n=int(input())
lst=list(int(i) for i in input().strip().split(' '))
k=int(input())
ans=kLargest(lst, k)
print(*ans, sep='\n')