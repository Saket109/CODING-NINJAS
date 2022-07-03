from sys import stdin

def findUnique(arr, n) :
    result = arr[0]
    for i in arr[1:]:
        result = result^i
    return result

def takeInput() :
    n = int(stdin.readline().strip())
    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


def printList(arr, n) : 
    for i in range(n) :
        print(arr[i], end = " ")
    print()


#main
t = int(stdin.readline().strip())
 
while t > 0 :
    
    arr, n = takeInput()
    print(findUnique(arr, n))

    t-= 1