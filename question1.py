
from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)

def lengthQ(inputQueue):
    count = 0
    while len(inputQueue) != 0:
        count+=1
        inputQueue.get()
    return count

def reverseQueue(inputQueue) :
    result = []
    while lengthQ:
        result.append(inputQueue(lengthQ(inputQueue)))
        inputQueue.get()

    return result



    
    


def takeInput():
    n = int(stdin.readline().strip())

    qu = queue.Queue()
    values = list(map(int, stdin.readline().strip().split()))

    for i in range(n) :
        qu.put(values[i])

    return qu


#main
t = int(stdin.readline().strip())

while t > 0 :
    
    qu = takeInput()
    reverseQueue(qu)
    
    while not qu.empty() :
        print(qu.get(), end = " ")
        
    print()
    
    t -= 1