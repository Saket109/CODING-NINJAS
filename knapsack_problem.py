# QUESTION : A thief robbing a store can carry a maximal weight of W into his knapsack. 
# There are N items, and i-th item weigh 'Wi' and the value being 'Vi.' What would be the
#  maximum value V, that the thief can steal?


from sys import stdin

def knapsack(weights, values, n, maxWeight,i) :
    # base case
    if i == n:
        return 0

    if weights[i]<=maxWeight:
        ans1 = knapsack(weights,values,n,maxWeight,i+1)
        ans2 = values[i] + knapsack(weights,values,n,(maxWeight-weights[i]),i+1)
        ans = max(ans1,ans2)
    else:
        ans = knapsack(weights,values,n,maxWeight,i+1)

    return ans



def takeInput() :
    n = int(stdin.readline().rstrip())

    if n == 0 :
        return list(), list(), n, 0

    weights = list(map(int, stdin.readline().rstrip().split(" ")))
    values = list(map(int, stdin.readline().rstrip().split(" ")))
    maxWeight = int(stdin.readline().rstrip())

    return weights, values, n, maxWeight


#main
weights, values, n, maxWeight = takeInput()

print(knapsack(weights, values, n, maxWeight,0))