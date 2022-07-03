class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
class BST:
    
    def __init__(self):
        self.root = None
        self.numNodes = 0
    
    def printTreehelper(self,root):
        if root is None:
            return
        print(root.data,end = " : ")
        if root.left is not None:
            print("L: ",root.left.data,end = " ")
        if root.right is not None:
            print("R: ",root.right.data)
        print()
        printTreehelper(root.left)
        printTreehelper(root.right)



    def printTree(self):
        printTreehelper(self.root)
    
    
    # def search(self, data):
    # ##################################
    # # PLEASE IMPLEMENT THIS FUNCTION #
    # ##################################

        
    # def insert(self, data):
    # ##################################
    # # PLEASE IMPLEMENT THIS FUNCTION #
    # ##################################
    
      
    # def delete(self, data):
    # ##################################
    # # PLEASE IMPLEMENT THIS FUNCTION #
    # ##################################
    
    # def count(self):
    #     return self.numNodes
        
b = BST()
q = int(input())
while (q > 0) :
    li = [int(ele) for ele in input().strip().split()]
    choice = li[0]
    q-=1
    if choice == 1:
        data = li[1]
        b.insert(data)
    elif choice == 2:
        data = li[1]
        b.delete(data)
    elif choice == 3:
        data = li[1]
        ans = b.search(data)
        if ans is True:
            print('true')
        else:
            print('false')
    else:
        b.printTree()