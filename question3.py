from sys import stdin

def pairSum(arr, n, num) :
    count = 0
    arr.sort()
    i = 0
    j = n-1
    while(i<j):
        if arr[i]+arr[j]==num:
            if arr[i]==arr[i+1] and arr[j]!=arr[j-1]:
                count+=1
                i+=1
            elif arr[j]==arr[j-1] and arr[i]!=arr[i+1]:
                count+=1
                j-=1
            elif arr[j]==arr[j-1] and arr[i]==arr[i+1]:
                extra1 = 1
                extra2 = 1
                while(i<n-1 and arr[i]==arr[i+1]):
                    extra1+=1
                    i+=1
                while(j>0 and arr[j]==arr[j-1]):
                    extra2+=1
                    j-=1
                if extra1==n:
                    count = (extra1*(extra1-1))//2
                    return count
                else:
                    n = extra1*extra2
                    count+=n
                    i+=1
                    j-=1
            else:
                count+=1
                i+=1
                j-=1
        elif arr[i]+arr[j]>num:
            j-=1
        else:
            i+=1
    return count


#taking input using fast I/O method
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
    num = int(stdin.readline().strip())
    print(pairSum(arr, n, num))

    t -= 1