
def answer(arr):
    ans1 = sum(arr)
    for i in arr:
        if 2*i in arr:
            arr.remove(2*i)

    ans2 = sum(arr)
    ans = (3*ans2-ans1)//2
    return ans

arr = [int(ele) for ele in input().split()]
print(answer(arr))
