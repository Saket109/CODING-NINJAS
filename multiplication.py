from sys import setrecursionlimit

def multiplication(m,n):
	setrecursionlimit(10**6)
	if n==0:
		return 0
	return m + multiplication(m,n-1)

m=int(input())
n=int(input())
print(multiplication(m,n))