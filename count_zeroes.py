def number_zeros(n):
    if n==0:
        return 0
    a=n%10
    x=n//10
    number_zeros(x)
    if a==0:
        return number_zeros(x) + 1
    else:
        return number_zeros(x)


n=int(input())
if n==0:
    print("1")
else:
    print(number_zeros(n))