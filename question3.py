from sys import stdin

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

def swap(prev,curr,future):
    temp = future.next
    prev.next = future
    future.next = curr
    curr.next = temp
    return prev

def bubbleSort(head,realhead) :
    
    while(head is not None):
        if head==realhead:
            temp = head.next
            head.next = head.next.next
            temp.next = head
            return head
        if head.data>head.next.data:
            swap(prev,head,head.next)
        prev = head
        head = head.next
    ans = bubbleSort(head,realhead)

def takeInput() :
    head = None
    tail = None

    datas = list(map(int, stdin.readline().rstrip().split(" ")))

    i = 0
    while (i < len(datas)) and (datas[i] != -1) :
        data = datas[i]
        newNode = Node(data)

        if head is None :
            head = newNode
            tail = newNode

        else :
            tail.next = newNode
            tail = newNode

        i += 1

    return head



def printLinkedList(head) :

    while head is not None :
        print(head.data, end = " ")
        head = head.next

    print()


#main
head = takeInput()
head = bubbleSort(head)
printLinkedList(head)