import heapq
def kSmallest(lst, k):
    list = lst[:k]
    heapq._heapify_max(list)
    for i in lst[k:]:
        val = heapq._heappop_max(list)
        if val > i:
            list.append(i)
            heapq._siftdown_max(list,0,len(list)-1)
        else:
            list.append(val)
            heapq._siftdown_max(list,0,len(list)-1)

    return list



# Main
n=int(input())
lst=list(int(i) for i in input().strip().split(' '))
k=int(input())
ans=kSmallest(lst, k)
ans.sort()
print(*ans, sep=' ')