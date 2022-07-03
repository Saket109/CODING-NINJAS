class BinaryTree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def takelevelinput():
    q = []
    rootdata = int(input())
    if rootdata==-1:
        return
    root = BinaryTree(rootdata)
    q.append(root)
    while len(q)!=0:
        curr_child = q[0]
        leftchild = int(input())
        rightchild = int(input())
        if leftchild!=-1:
            left_root = BinaryTree(leftchild)
            q.append(left_root)
            curr_child.left = left_root
        if rightchild!=-1:
            right_root = BinaryTree(rightchild)
            q.append(right_root)
            curr_child.right = right_root
        q.pop(0)

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
    

root = takelevelinput()
printTreeDetailed(root)