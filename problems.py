def heapSort(array):
    for i in range(len(array)//2,0):
        parentIndex = i

        while LchildIndex < len(array):
            LchildIndex = 2*parentIndex+1
            RchildIndex = 2*parentIndex+2
            if array[LchildIndex] < array[maxIndex]:
                maxIndex = LchildIndex
            if RchildIndex < len(array) and array[RchildIndex] < array[maxIndex]:
                maxIndex = RchildIndex
            if maxIndex == parentIndex:
                break
            array[maxIndex],array[parentIndex] = array[parentIndex],array[maxIndex]
            parentIndex = maxIndex
            

    for i in range(len(array)-1,0,-1):
        array[i],array[0] = array[0],array[i]
        parentIndex = 0
        LchildIndex = 2*parentIndex+1
        RchildIndex = 2*parentIndex+2
        maxIndex = parentIndex
        while LchildIndex<i:
            if array[maxIndex] > array[LchildIndex]:
                maxIndex = LchildIndex
            if RchildIndex < i and array[maxIndex] > array[RchildIndex]:
                maxIndex = RchildIndex
            if maxIndex == parentIndex:
                break
            array[maxIndex],array[parentIndex] = array[parentIndex],array[maxIndex]
            parentIndex = maxIndex
            LchildIndex = 2*parentIndex+1
            RchildIndex = 2*parentIndex+2



n = input()
arr = [int(ele) for ele in input().split()]
heapSort(arr)
for ele in arr:
    print(ele,end=' ')