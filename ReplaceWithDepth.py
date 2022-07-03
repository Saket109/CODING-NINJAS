from sys import stdin,setrecursionlimit
import queue
setrecursionlimit(10**6)

class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

i = 0
q = queue.Queue()

def replacewithDepth(tree,realtree):
    global i 
    if tree is None:
        return None
    tree.data = i
    q.put(tree)
    q.put("null")
    i+=1
    while(not (q.empty())):
        ans = q.get()
        if ans!="null":
            for child in ans.children:
                child.data = i
                q.put(child)
        else:
            i+=1
            if not q.empty():
                q.put("null")





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

def printLevelAtNewLine(tree):
    q = [tree]
    newq = []
    while q:
        parent = q.pop(0)
        print(parent.data, end=' ')
        for child in parent.children:
            newq.append(child)
        if len(q)==0:
            q = newq
            newq = []
            print()  # Move to next Line

# Main
arr = list(int(x) for x in stdin.readline().strip().split())
tree = createLevelWiseTree(arr)
replacewithDepth(tree,tree)
printLevelAtNewLine(tree)