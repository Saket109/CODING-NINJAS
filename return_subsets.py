## Read input as specified in the question.
## Print output as specified in the question.
def subsets(arr):
    # base case
    if len(arr) == 0:
        return [[]]

    ans1 = subsets(arr[1:])

    result = []

    for i in ans1:
        result.append(i)
        result.append([arr[0]]+i)

    return result

n= int(input())    
arr = [int(ele) for ele in input().split()]    
list = subsets(arr)
for l in list:
    print(l)