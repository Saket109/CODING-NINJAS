d = dict()
d[2] = "abc"
d[3] = "def"
d[4] = "ghi"
d[5] = "jkl"
d[6] = "mno"
d[7] = "pqrs"
d[8] = "tuv"
d[9] = "wxyz" 

def printkeypad(n,ans):
    # base case
    if n == 0:
        print(ans)
        return
    
    smallerInteger = n//10
    remainingInteger = n%10
    for i in d[remainingInteger]:
        printkeypad(smallerInteger,i+ans)


n = int(input())
printkeypad(n,"")