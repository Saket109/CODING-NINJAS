from sys import stdin,setrecursionlimit
setrecursionlimit(10**6)
class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

ans = 10000

def nextLargest(tree, n):
    global ans
    if tree is None:
        return None
    if tree.data>n and tree.data<ans:
        ans = tree.data
    for child in tree.children:
        if child.data>n and child.data<ans:
            ans = child.data
    for child in tree.children:
        nextLargest(child,n)
    if ans == 10000:
        return 
    return ans
    





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
arr = list(int(x) for x in stdin.readline().strip().split())
n = int(input())
tree = createLevelWiseTree(arr)
print(nextLargest(tree, n))