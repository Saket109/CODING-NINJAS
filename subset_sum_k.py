import sys
sys.setrecursionlimit(10 ** 8)


def subsetsSumK(arr, k) :
    if len(arr) == 0:
        return

    if k == arr[0]:
        return [arr[0]]

    output = []

    excluding_first = subsetsSumK(arr[1:],k)
    if excluding_first is not None:
        output.append(excluding_first)
    if arr[0]<=k:
        including_first = subsetsSumK(arr[1:],k-arr[0])
        if including_first is not None:
            ans = including_first
        output.append([arr[0]]+ans)

    return output

#taking input
def takeInput() :
    n = int(input().strip())

    if n == 0 :
        return list(), 0

    arr = [int(element) for element in list(input().strip().split(" "))]
    return arr, n


#printing the list of lists
def printListOfList(liOfLi) :
    for li in liOfLi :
        for elem in li :
            print(elem, end = " ")
        print()

#main
arr, n = takeInput()

if n != 0 :
    k = int(input().strip())
    liOfLi = subsetsSumK(arr, k)

    printListOfList(liOfLi)
