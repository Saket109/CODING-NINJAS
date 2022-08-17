## Read input as specified in the question.
## Print output as specified in the question.
def subsets(arr,ans):
    # base case
    if len(arr) == 0:
        if len(ans) == 0:
            print("[]")
        else:
            for i in ans:
                print(i,end = " ")
            print()
        return 

    # don't include
    subsets(arr[1:],ans)

    # do include
    subsets(arr[1:],ans+[arr[0]])

arr = [int(ele) for ele in input().split()]    
subsets(arr,[])