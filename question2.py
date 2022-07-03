from sys import stdin

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

def length (head):
    count = 0
    while head is not None:
        count+=1
        head = head.next
    return count

def reverse(head):
    if head is None or head.next is None:
        return head
    prev = head
    curr = head.next
    temp = curr.next
    while curr is not None:
        if prev is head :
            prev.next = None
        curr.next = prev
        prev = curr
        curr = temp
        if temp is not None:
            temp = curr.next
    return prev,head

def kReverse(head, k):
    if head is None:
        return None
    h1 = head
    t1 = head
    count = 1
    while count!=k and head.next is not None:
        t1 = head.next
        head = head.next
        count+=1
    h2 = t1.next
    t1.next = None
    h,t = reverse(h1)
    recursive_head = kReverse(h2,k)
    t.next = recursive_head
    return h


#Taking Input Using Fast I/O
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
t = int(stdin.readline().rstrip())

while t > 0 :
    
    head = takeInput()
    k = int(stdin.readline().strip())

    newHead = kReverse(head, k)
    printLinkedList(newHead)

    t -= 1