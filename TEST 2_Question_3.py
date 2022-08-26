class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

def deleteAlternateNodes(head):
    curr = head
    while curr is not None and curr.next is not None:
        curr.next = curr.next.next
        curr = curr.next
    return head

def ll(arr):
    if len(arr)==0:
        return None
    head = Node(arr[0])
    last = head
    for data in arr[1:]:
        last.next = Node(data)
        last = last.next
    return head

def printll(head):
    while head is not None:
        print(head.data,end= ' ')
        head = head.next
    return

# Main
# Read the link list elements including -1
arr=[int(ele) for ele in input().split()]
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
head = deleteAlternateNodes(l)
printll(head)