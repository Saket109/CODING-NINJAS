import sys
import queue
class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
    def __str__(self):
        return str(self.data)

q = queue.Queue()

def printLevelWiseTree(tree):
    if tree is None:
        return
    q.put(tree)

    while(not (q.empty())):
        ans = q.get()
        print(ans.data,end = ":")
        for child in ans.children:
            if child!=ans.children[-1]:
                print(child.data,end = ",")
            else:
                print(child.data,end = "")
            q.put(child)
        print()


        
        


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
sys.setrecursionlimit(10**6)
arr = list(int(x) for x in input().strip().split(' '))
tree = createLevelWiseTree(arr)
printLevelWiseTree(tree)