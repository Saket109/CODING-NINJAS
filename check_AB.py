def checkAB(s):
    if len(s)==0 :
        return True
    if s[0]=='a':
        if len(s[1:])>1 and s[1:3]=="bb":
            return checkAB(s[3:])
        if len(s[1:])>1 and s[1]=='a':
            return checkAB(s[1:])
        if len(s[1:])==1 and s[1]=='a':
            return True
        if len(s)==1:
            return True
    else:
        return False
    
s=input()
if checkAB(s):
    print("true")
else:
    print("false")