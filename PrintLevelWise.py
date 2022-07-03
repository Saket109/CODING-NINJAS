from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)


#Following is the structure used to represent the Binary Tree Node
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

q=[]

def printLevelWise(root):
    if root is None:
        return
    print(root.data,end=':')
    if root.left is not None:
        print(f"L:{root.left.data}",end=',')
    else:
        print(f"L:{-1}",end=',')
    if root.right is not None:
        print(f"R:{root.right.data}")
    else:
        print(f"R:{-1}")

    if root.left is not None:
        q.append(root.left)
    if root.right is not None:
        q.append(root.right) 

    while(len(q)!=0):
        root = q.pop(0)
        printLevelWise(root)
        
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


# Main
root = takeInput()
printLevelWise(root)