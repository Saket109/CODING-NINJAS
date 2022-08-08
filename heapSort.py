# Heap Sort is all about adding elements of an arrayay in the min heap and then get min 
#        from the heap and store it in the arrayay and that arrayay will be sorted.

# Time complexity is O(n) and Space complexity is O(1)
def heapSort(array):

    for i in range(1,len(array)):
        childIndex = i
        
        while childIndex>0:
            parentIndex = (i-1)//2
            if array[childIndex] > array[parentIndex]:
                array[childIndex],array[parentIndex] = array[parentIndex],array[childIndex]
                childIndex = parentIndex
            else:
                break

    print(array)
    for i in range(len(array)-1,0,-1):
        array[i],array[0] = array[0],array[i]
        parentIndex = 0
        LchildIndex = 2*parentIndex+1
        RchildIndex = 2*parentIndex+2
        maxIndex = parentIndex
        while LchildIndex<i:
            if array[maxIndex] < array[LchildIndex]:
                maxIndex = LchildIndex
            if RchildIndex < i and array[maxIndex] < array[RchildIndex]:
                maxIndex = RchildIndex
            if maxIndex == parentIndex:
                break
            array[maxIndex],array[parentIndex] = array[parentIndex],array[maxIndex]
            parentIndex = maxIndex
            LchildIndex = 2*parentIndex+1
            RchildIndex = 2*parentIndex+2


array = [int(ele) for ele in input().split()]
heapSort(array)
print(array)