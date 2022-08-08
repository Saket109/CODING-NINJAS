def unique(list):
    ans = list[0]
    for i in list[1:]:
        ans = ans ^ i
    return ans

list = [int(ele) for ele in input().split()]
print(unique(list))
