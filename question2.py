from sys import stdin


def findDuplicate(arr, n) :
    arr.sort()
    for i in range(n-1):
        if arr[i]==arr[i+1]:
            return arr[i]


#Taking input using fast I/O method
def takeInput() :
    n = int(stdin.readline().rstrip())

    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n


#main
t = int(stdin.readline().rstrip()) 

while t > 0 :

    arr, n = takeInput()
    print(findDuplicate(arr, n))

    t -= 1