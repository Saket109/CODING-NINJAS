import heapq
def kthLargest(lst, k):
    heap = lst[:k]
    heapq.heapify(heap)
    for i in lst[k:]:
        if heap[0] < i:
            heapq.heapreplace(heap,i)

    heapq._heapify_max(heap)    
    for i in range(k-1):
        heapq._heappop_max(heap)

    return heap[0]


# Main
n=int(input())
lst=list(int(i) for i in input().strip().split(' '))
k=int(input())
ans=kthLargest(lst, k)
print(ans)