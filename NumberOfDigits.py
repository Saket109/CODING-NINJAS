from math import log
def numberofdigits(n):
    return int(log(n,10)) + 1


n = int(input())
print(numberofdigits(n))