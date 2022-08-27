# Given two string s and t, write a function to check if s contains all characters of t (in the same order as they are in string t).
# Return true or false.
# Do it recursively.
# E.g. : s = “abchjsgsuohhdhyrikkknddg” contains all characters of t=”coding” in the same order. So function will return true.

def contains(s,t,m,n):
    if n==0:
        return True
    elif m==0:
        return False
    if s[m-1] == t[n-1]:
        return contains(s,t,m-1,n-1)
    return contains(s,t,m-1,n)
    
s = input()
t = input()

ans = contains(s,t,len(s),len(t))
if ans is True:
    print('true')
else:
    print('false')