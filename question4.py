from sys import stdin


def rotate(arr, n, d):
    arr.reverse()
    new_arr1 = arr[:n-d]
    new_arr1.reverse()
    new_arr2 = arr[n-d:]
    new_arr2.reverse()
    arr = new_arr1+new_arr2
    return arr



#Taking Input Using Fats I/O
def takeInput() :
    n = int(stdin.readline().rstrip())
    if n == 0:
        return list(), 0

    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n


#to print the array/list 
def printList(arr, n) : 
    for i in range(n) :
        print(arr[i], end = " ")
    print()


#main
t = int(stdin.readline().rstrip())

while t > 0 :
    
    arr, n = takeInput()
    d = int(stdin.readline().rstrip())
    result = rotate(arr, n, d)
    if n>0:
        printList(result, n)
    else:
        print()
    
    t -= 1