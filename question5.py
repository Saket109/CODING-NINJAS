from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)


#Following is the structure used to represent the Binary Tree Node
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def printnodesdepthk(root,k):
    if root is None:
        return
    if k==0:
        print(root.data)
        return
    printnodesdepthk(root.left,k-1)
    printnodesdepthk(root.right,k-1)

def nodesAtDistanceK(root, node, k, d) :
    if root is None:
        return -1
    if root.data == node:
        printnodesdepthk(root , k)
        return d
    ld = nodesAtDistanceK(root.left , node , k, d+1)
    if ld == -1:
        rd = nodesAtDistanceK(root.right, node , k , )
    print(ld)
    if ld==-1:
        d-=1
        rd = nodesAtDistanceK(root.right, node, k, d+1)
        print(rd)
        if rd+1 == k:
            print(root.data)
            return 
        if rd<k:
            printnodesdepthk(root.left, k-rd-2)
            return
    if ld+1 == k:
        print(root.data)
        return
    if ld<k:
        printnodesdepthk(root.right, k-ld-2)
        return

    

	


#Taking level-order input using fast I/O method
def takeInput():
    levelOrder = list(map(int, stdin.readline().strip().split(" ")))
    start = 0
    
    length = len(levelOrder)

    if length == 1 :
        return None
    
    root = BinaryTreeNode(levelOrder[start])
    start += 1

    q = queue.Queue()
    q.put(root)

    while not q.empty():
        currentNode = q.get()

        leftChild = levelOrder[start]
        start += 1

        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left =leftNode
            q.put(leftNode)

        rightChild = levelOrder[start]
        start += 1

        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right =rightNode
            q.put(rightNode)

    return root

    
def printLevelWise(root):
    if root is None:
        return

    inputQ = queue.Queue()
    outputQ = queue.Queue()
    inputQ.put(root)

    while not inputQ.empty():
       
        while not inputQ.empty():
       
            curr = inputQ.get()
            print(curr.data, end=' ')
            if curr.left!=None:
                outputQ.put(curr.left)
            if curr.right!=None:
                outputQ.put(curr.right)
       
        print()
        inputQ, outputQ = outputQ, inputQ


# Main
root = takeInput()
target_k = stdin.readline().strip().split(" ")

target = int(target_k[0])
k = int(target_k[1])

nodesAtDistanceK(root, target, k, 0)