
        
def printPermutations(string,ans):
    # base case
    if len(string) == 0:
        print(ans)
        return 

    for j in range(len(string)):
            prev = string[0:j]
            curr = string[j]
            next = string[j+1:]
            printPermutations(prev+next,ans+curr)

        


string = input()
printPermutations(string,"")