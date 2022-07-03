def nodetorootpath(root,k):
    if root is None:
        return None

    if root.data == k:
        s=[]
        s.append(root.data)
        return s

    leftoutput = nodetorootpath(root.left,k)
    if leftoutput is not None:
        leftoutput.append(root.data)
        return leftoutput

    rightoutput = nodetorootpath(root.right,k)
    if rightoutput is not None:
        rightoutput.append(root.data)
        return rightoutput
    else:
        return None

