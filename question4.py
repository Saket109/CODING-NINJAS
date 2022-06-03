
from sys import stdin

def stockSpan(price, n) :
	s = []
	result = []

	for i in range(n):
		if i==0:
			result.append(1)
			s.append(i)
		else:
			if price[i]<price[s[0]]:
				if price[i]==price[s[-1]]:
					result.append(1)
				elif price[i]<price[s[-1]]:
					result.append(1)
					s.append(i)
				else:
					while (price[i]>price[s[-1]]):
						s.pop()
					result.append(i-(s[-1]))
					s.append(i)
			elif price[i]==price[s[0]]:
				result.append(1)
			else:
				s.pop()
				s.append(i)
				result.append(i+1)
	
	return result




'''-------------- Utility Functions --------------'''




def printList(arr) :
	for i in range(len(arr)) :
		print(arr[i], end = " ")

	print()


def takeInput():
	size = int(stdin.readline().strip())

	if size == 0 :
		return list(), 0

	price = list(map(int, stdin.readline().strip().split(" ")))

	return price, size


#main
price, n = takeInput()

output = stockSpan(price, n)
printList(output)