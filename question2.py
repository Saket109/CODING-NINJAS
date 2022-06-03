
from sys import stdin

def checkRedundantBrackets(expression) :
    s = []
    for char in expression:
            if char == ')':
                top = s[-1]
                s.pop()

                flag = True

                while (top!='('):
                    if top in '/-*+':
                        flag = False

                    top = s[-1]
                    s.pop()

                if flag == True :
                    return True

            else:
                s.append(char)

    return False

    

#main
expression = stdin.readline().strip()

if checkRedundantBrackets(expression) :
	print("true")

else :
	print("false")