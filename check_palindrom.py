def reverse(s):
    if len(s)==0 or len(s)==1:
        return s
    a=s[1:]
    new_s=reverse(a)
    return new_s+s[0]

def check_palindrome(s):
	if reverse(s) == s:
		print("true")
	else:
		print("false")
    
s=input()
check_palindrome(s)