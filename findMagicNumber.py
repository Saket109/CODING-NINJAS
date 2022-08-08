# if binary is 0101 then change it to base 5 so answer should look like :
    # 1*5 + 0*5^2 + 1*5^3 + 0*5^4  =  130

def MagicNumber(n):
    base = 5
    ans = 0
    while n>0 :
        val = n&1
        ans = ans + val*base
        n = n>>1
        base = base*5

    return ans

print(MagicNumber(5))