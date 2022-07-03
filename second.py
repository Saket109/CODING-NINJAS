
def checking(s):
    numericals = 0
    lowercases = 0
    uppercases = 0
    for i in range(len(s)):
        if s[i] in ['0','1','2','3','4','5','6','7','8','9']:
            numericals+=1
        elif s[i].islower() is True:
            lowercases+=1
        elif s[i].isupper() is True:
            uppercases+=1
            
    if numericals>=1 and lowercases>=1 and uppercases>=1:
        return True
    else:
        return False
 
t = int(input())

while(t>0):
    s = input()
    if checking(s):
        print("YES")
    else:
        print("NO")
    t-=1