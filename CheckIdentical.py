from sys import stdin,setrecursionlimit
setrecursionlimit(10**6)
class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

def isIdentical(tree1, tree2):
    if tree1 is None and tree2 is None:
        return True
    if tree1 is None and tree2 is not None:
        return False
    if tree1 is not None and tree2 is None:
        return False
    if len(tree1.children)!=len(tree2.children):
        return False
    for i in range(len(tree1.children)):
        childof1 = tree1.children[i]
        childof2 = tree2.children[i]
        if childof1.data != childof2.data:
            return False
    for i in range(len(tree1.children)):
        childof1 = tree1.children[i]
        childof2 = tree2.children[i]
        ans = isIdentical(childof1,childof2)
        if ans is False:
            return False
    return True

    





def createLevelWiseTree(arr):
    root = treeNode(int(arr[0]))
    q = [root]
    size = len(arr)
    i = 1
    while i<size:
        parent = q.pop(0)
        childCount = int(arr[i])
        i += 1
        for j in range(0,childCount):
            temp = treeNode(int(arr[i+j]))
            parent.children.append(temp)
            q.append(temp)
        i += childCount
    return root

# Main
arr1 = list(int(x) for x in stdin.readline().strip().split())
tree1 = createLevelWiseTree(arr1)
arr2 = list(int(x) for x in stdin.readline().strip().split())
tree2 = createLevelWiseTree(arr2)
if isIdentical(tree1, tree2):
    print('true')
else:
    print('false')