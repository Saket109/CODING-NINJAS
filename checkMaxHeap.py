def checkMaxHeap(lst):
    for i in range(len(lst)):
        parentIndex = i
        LchildIndex = 2*parentIndex+1
        RchildIndex = 2*parentIndex+2

        if (LchildIndex<len(lst) and lst[parentIndex] < lst[LchildIndex]) or (RchildIndex<len(lst) and lst[parentIndex] < lst[RchildIndex]) : 
            return False
        
    return True


# Main Code
n=int(input())
lst=list(int(i) for i in input().strip().split(' '))
print('true') if checkMaxHeap(lst) else print('false')