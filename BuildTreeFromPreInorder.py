class BinaryTree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def printTreeDetailed(root):
    if root is None:
        return None
    if root.left is not None or root.right is not None:
        print(root.data,end= ":")
    if root.left is not None:
        print("L:",root.left.data,end=",")
    if root.right is not None:
        print("R:",root.right.data)
    printTreeDetailed(root.left)
    printTreeDetailed(root.right)
    return 


def buildtreefrompreIn(pre,inorder):
    if len(pre) == 0:
        return None
    rootdata = pre[0]
    root = BinaryTree(rootdata)
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

pre = [1,2,4,5,3,6,7]
inorder = [4,2,5,1,6,3,7]
root = buildtreefrompreIn(pre,inorder)
printTreeDetailed(root)