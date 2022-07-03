import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

s=[]

def elementsInRangeK1K2(root, k1, k2):
    if root is None:
        return 
    if root.data<k1:
        elementsInRangeK1K2(root.right,k1,k2)
    elif root.data>k2:
        elementsInRangeK1K2(root.left,k1,k2)
    else:
        s.append(root.data)
        elementsInRangeK1K2(root.left,k1,k2)
        elementsInRangeK1K2(root.right,k1,k2)
    return s


def buildLevelTree(levelorder):
    index = 0
    length = len(levelorder)
    if length<=0 or levelorder[0]==-1:
        return None
    root = BinaryTreeNode(levelorder[index])
    index += 1
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        currentNode = q.get()
        leftChild = levelorder[index]
        index += 1
        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left =leftNode
            q.put(leftNode)
        rightChild = levelorder[index]
        index += 1
        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right =rightNode
            q.put(rightNode)
    return root

# Main
levelOrder = [int(i) for i in input().strip().split()]
root = buildLevelTree(levelOrder)
k1, k2 = (int(i) for i in input().strip().split())
mylist = elementsInRangeK1K2(root, k1, k2)
if mylist is not None:
    mylist.sort()

if mylist is None:
    print()
else:
    for ele in mylist :
        print(ele,end = " ")
