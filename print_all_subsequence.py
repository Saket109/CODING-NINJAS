def printsubsequence(str,ans):
    # base case 
    if len(str) == 0:
        print(ans)
        return
    
    printsubsequence(str[1:],ans)
    printsubsequence(str[1:],ans+str[0])

str = input()
printsubsequence(str,"")