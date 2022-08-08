# QUESTION : Find the unique element if other than it every number appears thrice.

def unique(arr):
    result = 0
    for i in range(32):
        x = 1<<i
        sm = 0

        for j in range(len(arr)):
            if arr[j]&x:
                sm += 1

        if (sm%3) != 0:
            result = result | x

    return result

arr = [int(ele) for ele in input().split()]
print(unique(arr))