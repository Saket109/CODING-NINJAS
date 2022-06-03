class BinaryTree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def printTree(root):
    if root is None:
        return None
    print(root.data)
    if root.left is not None:
        print("L",root.left.data,end = ",")
    if root.right is not None:
        print("R",root.right.data)
    printTree(root.left)
    printTree(root.right)

def takeinput():
    rootdata = int(input())
    if rootdata == -1:
        return None
    root = BinaryTree(rootdata)
    rootleft = takeinput()
    rootright = takeinput()
    root.left = rootleft
    root.right = rootright
    return root

def countNodes(root):
    if root is None:
        return 0
    leftcount = countNodes(root.left)
    rightcount = countNodes(root.right)
    return leftcount+rightcount+1

root = takeinput()
print(countNodes(root))