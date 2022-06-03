from sys import stdin

def isBalance(expression):
    s = []
    for i in expression:
        if i in '({[':
            s.append(i)
        elif i is ')':
            if (not s or s[-1]!='('):
                return False
            s.pop()
        elif i is ']':
            if (not s or s[-1]!='['):
                return False
            s.pop()
        elif i is '}':
            if (not s or s[-1]!='{'):
                return False
            s.pop()

    if (not s):
        return True
    return False

    return True



expression = stdin.readline().strip()

if isBalance(expression):
    print("true")
else:
    print("false")
