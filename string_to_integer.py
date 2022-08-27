def integer(s):
    if len(s)==0:
        return -1
    if len(s)==1:
        return int(s)
    a=int(s[len(s)-1])
    x=integer(s[:len(s)-1])
    return 10*x+a
    
s=input()
print(integer(s))