
from sys import stdin
import queue

def reverseQueue(qu):
    stack = []
    stack.append(qu.get())
    qu.put(stack.pop())

def lengthQueue(qu) :
    count = 0
    while qu:
        count += 1
        qu.get()
    return count

def reverseKElements(inputQueue, k) :
    n = lengthQueue(inputQueue)
    for i in range(k) :
        reverseQueue(inputQueue)
    
    for j in range(n-k):
        val = inputQueue.get()
        inputQueue.put(val)

'''-------------- Utility Functions --------------'''


#Takes a list as a stack and returns whether the stack is empty or not
def isEmpty(stack) :
    return len(stack) == 0


#Takes a list as a stack and returns the element at the top
def top(stack) :
    #assuming the stack is never empty
    return stack[len(stack) - 1]



def takeInput():
    n_k = list(map(int, stdin.readline().strip().split(" ")))
    n = n_k[0]
    k = n_k[1]

    qu = queue.Queue()
    values = list(map(int, stdin.readline().strip().split()))

    for i in range(n) :
        qu.put(values[i])

    return k, qu


#main
k, qu = takeInput()

qu = reverseKElements(qu, k)

while not qu.empty() :
    print(qu.get(), end = " ")