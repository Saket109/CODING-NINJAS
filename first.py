from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)


#Following is the structure used to represent the Binary Tree Node
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def takeinput():
    rootdata = int(input())
    if rootdata == -1:
        return None
    root = BinaryTreeNode(rootdata)
    rootleft = takeinput()
    rootright = takeinput()
    root.left = rootleft
    root.right = rootright
    return root

def printTreeDetailed(root):
    if root is None:
        return
    if root.left is not None or root.right is not None:
        print(root.data,end = ':')
    if root.left is not None:
        print("L",root.left.data,end = ',')
    if root.right is not None:
        print("R",root.right.data)
    printTreeDetailed(root.left)
    printTreeDetailed(root.right)

def removeleaves(root):
    if root is None:
        return None
    if root.left is None and root.right is None:
        return None
    root.left = removeleaves(root.left)
    root.right = removeleaves(root.right)
    return root

# Main
root = takeinput() 
root = removeleaves(root)
printTreeDetailed(root)

