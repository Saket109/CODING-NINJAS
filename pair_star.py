def pairstar(s):
    if len(s)==0 or len(s)==1:
        return s
    a=s[0]
    x=s[1:]
    q=pairstar(x)
    if a == x[0]:
        return a+'*'+q
    else:
        return a+q
    
s=input()
print(pairstar(s))