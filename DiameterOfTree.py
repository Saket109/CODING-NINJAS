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

def Diameter(root):
    if root is None:
        return 0,0
    lh,ld = Diameter(root.left)
    rh,rd = Diameter(root.right)
    return 1+max(lh,rh),max(lh+rh,ld,rd)

root = takeinput()
print(Diameter(root))  