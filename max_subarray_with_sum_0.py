def maxLen(arr):
    hash_map = {}
    max_len = 0
    curr_sum = 0

    for i in range(len(arr)):
        curr_sum += arr[i]
 
        if arr[i] == 0 and max_len == 0:
            max_len = 1
 
        if curr_sum == 0:
            max_len = i + 1

        if curr_sum in hash_map:
            max_len = max(max_len, i - hash_map[curr_sum])
        else:
            hash_map[curr_sum] = i
 
    return max_len
 

 # Main
n=int(input())
l=list(int(i) for i in input().strip().split(' '))
print(maxLen(l))