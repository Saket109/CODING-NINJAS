## Read input as specified in the question.
## Print output as specified in the question.
# Problem ID 328 Midpoint LL
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverseList(head):
    if not head:
        return
    curNode = head
    prevNode = head
    nextNode = head.next
    curNode.next = None
  
    while(nextNode):
        curNode = nextNode
        nextNode = nextNode.next
        curNode.next = prevNode
        prevNode = curNode
  
    return curNode


def nextNumber(head):
    head = reverseList(head)
    k = head
    carry = 0
    prev = None
    head.data += 1
  
    # update carry for next calculation
    while(head != None) and (head.data > 9 or carry > 0):
        prev = head
        head.data += carry
        carry = head.data // 10
        head.data = head.data % 10
        head = head.next
  
    if carry > 0:
        prev.next = Node(carry)
    # Reverse the modified list
    return reverseList(k)


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
head = nextNumber(l)
printll(head)