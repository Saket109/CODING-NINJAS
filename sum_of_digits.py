def number_digits(n):
    count=1
    while n//10:
        count+=1
        n=n//10
    return count

def sum_digits(n):
    if n==0:
        return 0
    number=number_digits(n)
    a=n//(10**(number-1))
    x=n%(10**(number-1))
    sum_digits(x)
    return a+sum_digits(x)

n=int(input())
print(sum_digits(n))