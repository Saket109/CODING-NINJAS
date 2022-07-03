from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)


#Following is the structure used to represent the Binary Tree Node
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



def buildtreefrompreIn(pre,inorder):
    if len(pre) == 0:
        return None
    rootdata = pre[0]
    root = BinaryTreeNode(rootdata)
    rootininorder = -1
    for i in range(0,len(inorder)):
        if inorder[i]==rootdata:
            rootininorder = i
    if rootininorder == -1:
        return None
    leftinorder = inorder[:rootininorder]
    rightinorder = inorder[rootininorder+1:]
    leftpreorder = pre[1:len(leftinorder)+1]
    rightpreorder = pre[len(leftinorder)+1:]
    leftchild = buildtreefrompreIn(leftpreorder,leftinorder)
    rightchild = buildtreefrompreIn(rightpreorder,rightinorder)
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

    preOrder = list(map(int, stdin.readline().strip().split(" ")))
    inOrder = list(map(int, stdin.readline().strip().split(" ")))

    return preOrder, inOrder, n


# Main
preOrder, inOrder, n = takeInput()
root = buildtreefrompreIn(preOrder, inOrder, n)
printLevelWise(root)