class BinaryTree:
    def __init__(self,data):
        self.data = data
        self.left = None 
        self.right = None

def takeinput():
    n = int(input())
    if n==-1:
        return 
    root = BinaryTree(n)
    root.left = takeinput()
    root.right = takeinput()
    return root

def printtree(root):
    if root is None:
        return
    if root.left is not None or root.right is not None:
        print(root.data,end = ":")
    if root.left is not None:
        print("L",root.left.data,end = ",")
    if root.right is not None:
        print("R",root.right.data)
    printtree(root.left)
    printtree(root.right)
    return

def height(root):
    if root is None:
        return 0
    left_height = height(root.left)
    right_height = height(root.right)
    return 1+max(left_height,right_height)


def checkbalanced(root):
    if root is None:
        return True
    if height(root.left)-height(root.right)>1 or height(root.right)-height(root.right)>1:
        return False
    left = checkbalanced(root.left)
    right = checkbalanced(root.right)
    return left and right

root = takeinput()
print(checkbalanced(root))