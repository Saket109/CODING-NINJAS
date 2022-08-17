d = dict()
d[2] = "abc"
d[3] = "def"
d[4] = "ghi"
d[5] = "jkl"
d[6] = "mno"
d[7] = "pqrs"
d[8] = "tuv"
d[9] = "wxyz"
def keypad(n):
    # base case
    if n == 0:
        return [""]
    smallerInteger = n//10
    remainingInteger = n%10
    smallerOutput = keypad(smallerInteger)
    output = []

    for i in smallerOutput:
        for j in d[remainingInteger]:
            output.append(i+j)

    return output


n = int(input())
ans = keypad(n)
for s in ans:
    print(s)