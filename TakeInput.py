class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = list()

def takeinput():
    root_data = int(input("ENTER THE ROOT DATA  "))
    if root_data == -1:
        return None
    root = TreeNode(root_data)
    print("ENTER THE NUMBER OF CHILDREN OF ",root_data)
    t = int(input())
    for i in range(t):
        child = takeinput()
        root.children.append(child)
    
    return root


def printTree(root):
    if root is None:
        return 
    print(root.data,end = " : ")
    for child in root.children:
        print(child.data,end = ",")
    print()
    for child in root.children:
        printTree(child)

root = takeinput()
printTree(root)
