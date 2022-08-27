# Given an integer array A of size N, check if the input array can be splitted in two parts such that -
# - Sum of both parts is equal
# - All elements in the input, which are divisible by 5 should be in same group.
# - All elements in the input, which are divisible by 3 (but not divisible by 5) should be in other group.
# - Elements which are neither divisible by 5 nor by 3, can be put in any group.
# Groups can be made with any set of elements, i.e. elements need not to be continuous. And you need to consider each and every element of input array in some group.
# Return true, if array can be split according to the above rules, else return false.
# Note : You will get marks only if all the test cases are passed.
# Input Format :
# Line 1 : Integer N (size of array)
# Line 2 : Array A elements (separated by space)

def helper(arr, n, start, lsum, rsum):
    if (start == n):
        return lsum == rsum
 
    if (arr[start] % 5 == 0):
        lsum += arr[start]
 
    elif (arr[start] % 3 == 0):
        rsum += arr[start]

    else:
        return (helper(arr, n, start + 1,lsum + arr[start], rsum) or helper(arr, n, start + 1,lsum, rsum + arr[start]))
        
    return helper(arr, n, start + 1, lsum, rsum)
 
def split(arr, n):
    return helper(arr, n, 0, 0, 0)
    
n = input()
arr = [int(ele) for ele in input().split()]
ans = split(arr,len(arr))
if ans is True:
    print('true')
else:
    print('false')