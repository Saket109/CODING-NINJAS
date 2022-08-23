from sys import stdin

def stockSpan(price, n) :
    s = []
    result = []
    for i in range(n):
        if i == 0:
            s.append(i)
            result.append(1)
        else:
            while len(s)>0 :
                val = s.pop()
                if price[i] > price[val] :
                    ans = i+1
                elif price[i] <= price[val] :
                    ans = i-val
                    if price[i] < price[val] :
                        s.append(val)
                    else:
                        pass
                    break
            s.append(i)
            result.append(ans)


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