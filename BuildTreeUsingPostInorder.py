from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)


#Following is the structure used to represent the Binary Tree Node
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



def buildTree(postOrder, inOrder,n) :
    if n==0:
        return None
    rootdata = postOrder[n-1]
    root = BinaryTreeNode(rootdata)
    for i in range(n):
        if rootdata == inOrder[i]:
            rootininorder = i
    leftinorder = inOrder[:rootininorder]
    rightinorder = inOrder[rootininorder+1:]
    leftpostorder = postOrder[:len(leftinorder)]
    rightpostroder = postOrder[len(leftinorder):n]
    leftchild = buildTree(leftpostorder,leftinorder)
    rightchild = buildTree(rightpostroder,rightinorder)
    root.left = leftchild
    root.right = rightchild
    return root

def printLevelWise(root):
    if root is None :
        return

    pendingNodes = queue.Queue()
    pendingNodes.put(root)
    pendingNodes.put(None)

    while not pendingNodes.empty(): 
        frontNode = pendingNodes.get()
    
        if frontNode is None :
            print()
            
            if not pendingNodes.empty() :
                pendingNodes.put(None)
                
        else :
            print(frontNode.data, end = " ")
            
            if frontNode.left is not None :
                pendingNodes.put(frontNode.left)
                
                
            if frontNode.right is not None :
                pendingNodes.put(frontNode.right)


#Taking level-order input using fast I/O method
def takeInput():
    n = int(stdin.readline().strip())

    if n == 0 :
        return list(), list(), 0

    postOrder = list(map(int, stdin.readline().strip().split(" ")))
    inOrder = list(map(int, stdin.readline().strip().split(" ")))

    return postOrder, inOrder, n


# Main
postOrder, inOrder, n = takeInput()
root = buildTree(postOrder, inOrder,n)
printLevelWise(root)