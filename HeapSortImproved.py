def down_heapify(array,i,n):
    parentIndex=i
    LChildIndex=2*parentIndex+1
    RChildIndex=2*parentIndex+2
    
    while LChildIndex<n:
        minIndex=parentIndex
        if array[minIndex]>array[LChildIndex]:
            minIndex=LChildIndex
        if RChildIndex<n and array[minIndex]>array[RChildIndex]:
            minIndex=RChildIndex
        if minIndex==parentIndex:
            return 
        array[minIndex],array[parentIndex]=array[parentIndex],array[minIndex]
        parentIndex = minIndex
        LChildIndex = 2*parentIndex+1
        RChildIndex = 2*parentIndex+2
    return

def heapSort(array):
    #Build the heap
     n = len(array)
     for i in range(n//2,-1,-1):
            down_heapify(array,i,n)
            
     for i in range(n-1,0,-1):
        array[0],array[i]=array[i],array[0]
        down_heapify(array,0,i)
     return 
    
    #Removing n elements from the heap and put them at carrayect position
arr = [int (ele)for ele in input().split()]
heapSort(arr)
for ele in arr[::-1]:
    print(ele,end=" ")