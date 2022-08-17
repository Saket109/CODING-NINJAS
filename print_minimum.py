import sys
def minimum(arr,ans):
    if len(arr) == 1:
        if ans > arr[0]:
            print(arr[0])
        else:
            print(ans)
        return
    if ans > arr[0]:
        ans = arr[0]
    minimum(arr[1:],ans)

arr = [int(ele) for ele in input().split()]
minimum(arr,sys.maxsize)