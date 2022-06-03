class BinaryTree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def printTree(root):
# Base Case:
    if root is None:
        return

    print(root.data)
    printTree(root.left)
    printTree(root.right)

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


btn1 = BinaryTree(1)
btn2 = BinaryTree(2)
btn3 = BinaryTree(3)
root = btn1
btn1.left = btn2
btn1.right = btn3

printTreeDetailed(root)

    