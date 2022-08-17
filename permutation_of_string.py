
def permutations(string):
    # base case
    if len(string) == 0:
        return [""]

    ans = permutations(string[1:])
    result = []
    for i in ans:
        for j in range(len(i)+1):
            prev = i[0:j]
            curr = string[0]
            next = i[j:]
            result.append(prev+curr+next)

    return result

string = input()
n = len(string)
ans = permutations(string)
for s in ans:
    print(s)
