
from sys import stdin

def countBracketReversals(inputString) :
    s = []
    if len(inputString) % 2 == 0:
        count = 0
        for i in inputString :
            if i == "{" :
                s.append(i)
            elif i == "}" :
                if len(s) == 0:
                    count += 1
                    s.append("{")
                else:
                    s.pop()
        return count+len(s)//2
    else:
        return -1


#main
print(countBracketReversals(stdin.readline().strip()))