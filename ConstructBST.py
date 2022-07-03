import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def constructBST(lst):
    rootindex = (len(lst)-1)//2
    if len(lst)==0:
        return 
    root = BinaryTreeNode(lst[rootindex])
    if len(lst)==1:
        return root
    leftchild = constructBST(lst[:rootindex])
    rightchild = constructBST(lst[rootindex+1:])
    root.left = leftchild
    root.right = rightchild
    return root



def preOrder(root):
    # Given a binary tree, print the preorder traversal of given tree. Pre-order
    # traversal is: Root LeftChild RightChild
    if root==None:
        return
    print(root.data, end=' ')
    preOrder(root.left)
    preOrder(root.right)

# Main
n=int(input())
if(n>0):
    lst=[int(i) for i in input().strip().split()]
else:
    lst=[]
root=constructBST(lst)
preOrder(root)
