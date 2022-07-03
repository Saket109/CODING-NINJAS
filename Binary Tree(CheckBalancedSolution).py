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


def checkbalanced(root):
    if root is None:
        return 0,True
    lh,isbalancedleft = checkbalanced(root.left)
    rh,isbalancedright = checkbalanced(root.right)
    h = 1+max(lh,rh)
    if lh-rh>1 or rh-lh>1:
        return h,False
    if isbalancedleft and isbalancedright:
        return h,True
    else:
        return h,False
       

root = takeinput()
print(checkbalanced(root))