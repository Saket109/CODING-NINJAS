# You have made a smartphone app and want to set its subscription price such that the profit earned is maximised. There are certain users who will subscribe to your app only if their budget is greater than or equal to your price.
# You will be provided with a list of size N having budgets of subscribers and you need to return the maximum profit that you can earn.
# Lets say you decide that price of your app is Rs. x and there are N number of subscribers. So maximum profit you can earn is :
#  m * x
# where m is total number of subscribers whose budget is greater than or equal to x.

def partition(a,si,ei):
    count=0
    i=si
    j=ei
    for k in range(si,ei+1):
        if a[si]>a[k]:
            count+=1
    a[si+count],a[si]=a[si],a[si+count]
    while i<j:
        if a[si+count]>a[i]:
            i+=1
        elif a[si+count]<=a[j]:
                j-=1
        else:
            a[i],a[j]=a[j],a[i]
            i+=1
            j-=1
    return si+count 

def quickSort(a,si,ei):
    if si>=ei:
        return
    i=partition(a,si,ei)
    quickSort(a,si,i-1)
    quickSort(a,i+1,ei)


def maximumProfit(arr):
    quickSort(arr,0,len(arr)-1)
    empty_list=[]
    for i in range(len(arr)):
        empty_list.append((arr[i])*(len(arr)-i))
    quickSort(empty_list,0,len(empty_list)-1)
    return empty_list[-1]

n = int(input())
arr = [int(ele) for ele in input().split()]
ans = maximumProfit(arr)
print(ans)