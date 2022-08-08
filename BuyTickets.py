# QUESTION : You want to buy a ticket for a well-known concert which is happening in your city. But the number of tickets available is limited. Hence the sponsors of the concert decided to sell tickets to customers based on some priority.
# A queue is maintained for buying the tickets and every person is attached with a priority (an integer, 1 being the lowest priority).
# The tickets are sold in the following manner -
# 1. The first person (pi) in the queue requests for the ticket.
# 2. If there is another person present in the queue who has higher priority than pi, then ask pi to move at end of the queue without giving him the ticket.
# 3. Otherwise, give him the ticket (and don't make him stand in queue again).
# Giving a ticket to a person takes exactly 1 minute and it takes no time for removing and adding a person to the queue. And you can assume that no new person joins the queue.
# Given a list of priorities of N persons standing in the queue and the index of your priority (indexing starts from 0). Find and return the time it will take until you get the ticket.

from sys import stdin
import sys
import heapq as heap

class LinkedListNode :
    def __init__(self, data) :
        self.data = data
        self.next = None
        
class Queue :
    def __init__(self) :
        self.head = None 
        self.tail = None
        self.size = 0
        
    def enqueue(self, data) :
        newNode = LinkedListNode(data)
        if self.head is None :
            self.head = self.tail = newNode
        else :
            self.tail.next = newNode
            self.tail = newNode
        self.size += 1
        return
        
    def dequeue(self) :
        if self.head is None :
            return None
        data = self.head.data
        self.head = self.head.next
        self.size -= 1
        return data
    
    def getSize(self) :
        return self.size
    
    def isEmpty(self) :
        if self.head is None :
            return True
        return False
    
    def peek(self) :
        if self.head is None :
            return None
        return self.head.data
    
def buyTicket(arr, n, k) :
    ans = 0
    myqueue = Queue()
    myheap = []
    heap._heapify_max(myheap)
    for i in range(len(arr)):
        myqueue.enqueue(i)
        myheap.append(arr[i])
        heap._siftdown_max(myheap,0,len(myheap)-1)

    while i > -1:

        val = myqueue.dequeue()

        if arr[val] == myheap[0]:
            ans += 1
            heap._heappop_max(myheap)
            if val == k:
                return ans
        else:
            myqueue.enqueue(val)

    return ans

#taking input using fast I/O
def takeInput() :
    n = int(stdin.readline().strip())
    if n == 0 :
        return n, list(), int(stdin.readline().strip())
    arr = list(map(int, stdin.readline().strip().split(" ")))
    k = int(stdin.readline().strip())
    return n, arr, k

#main
sys.setrecursionlimit(10**6)
n, arr, k = takeInput()
print(buyTicket(arr, n, k))