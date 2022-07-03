import sys

#main
sys.setrecursionlimit(10**6)

class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = list()

def createTree(arr):
    rootdata = arr[0]
    if rootdata == -1:
        return None
    root = TreeNode(rootdata)
    i = 1
    size = len(arr)
    while(i<size):
        children_count = arr[i]
        i+=1
        for j in range(0,children_count):
            child_data = arr[i+j]
            child = TreeNode(child_data)
            root.children.append(child)
        i+=children_count
    return root

ans = 0

def heightOfTree(root):
    global ans
    if root is None:
        return 0
    ans=1
    for child in root.children:
        if ans<=heightOfTree(child):
            ans = ans + heightOfTree(child)
    
    return ans

arr = list(int(x) for x in input().strip().split(' '))
root = createTree(arr)
print(heightOfTree(root))