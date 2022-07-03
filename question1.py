from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)

#Following is the Node class already written for the Linked List
class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

def mergeTwoSortedLinkedLists(head1, head2):
    fh = None
    ft = None
    while head1 is not None and head2 is not None:
        if head1.data<head2.data:
            if fh is None and ft is None:
                fh = head1
                ft = head1
            else:
                ft.next = head1
                ft = ft.next
            head1 = head1.next

        else:
            if fh is None and ft is None:
                fh = head2
                ft = head2  
            else:          
                ft.next = head2
                ft = ft.next
            head2 = head2.next
    while head1 is not None:
        if fh is None and ft is None:
            fh = head1
            ft = head1
        else:
            ft.next = head1
            ft = ft.next
        head1 = head1.next
    while head2 is not None:
        if fh is None and ft is None:
            fh = head1
            ft = head1
        else:
            ft.next = head2
            ft = ft.next 
        head2 = head2.next

    return fh           

def lengthll(head):
    count = 0
    while(head is not None):
        count+=1
        head = head.next
    return count

def mergeSort(head):
    if head is None:
        return head
    if head.next is None:
        return head
    height = lengthll(head)
    head1 = head
    mid = head
    midpoint = (height+1)//2
    for _ in range(1,midpoint):
        mid = head.next
        head = head.next
    head2 = mid.next
    mid.next = None
    leftpart = mergeSort(head1)
    rightpart = mergeSort(head2)
    required = mergeTwoSortedLinkedLists(leftpart,rightpart)
    return required


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

    newHead = mergeSort(head)
    printLinkedList(newHead)

    t -= 1