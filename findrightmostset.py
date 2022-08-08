def findrightmostsetbit(n):
    count = 1
    while (n&1 == 0):
        count += 1
        n = n>>1

    return count 

n = int(input())
print(findrightmostsetbit(n))
