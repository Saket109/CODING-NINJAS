import queue

class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = list()

q = queue.Queue()

def takeinputlevelwise():
    rootdata = int(input())
    if rootdata == -1:
        return None
    root = TreeNode(rootdata)
    q.put(root)
    while(not (q.empty())):
        like = q.get()
        print("enter number of children of ",like.data)
        n = int(input())
        for i in range(n):
            childdata = int(input())
            child = TreeNode(childdata)
            like.children.append(child)
            q.put(child)

    return root

def printTree(root):
    if root is None:
        return None
    print(root.data,end = " : ")
    for child in root.children:
        print(child.data,end = ",")
    print()
    for child in root.children:
        printTree(child)

root = takeinputlevelwise()
printTree(root)