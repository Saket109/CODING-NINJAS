

def subsequences(string):
    if len(string) == 0:
        return [""]
    output = []
    for i in subsequences(string[1:]):
        output.append(i)
    for i in subsequences(string[1:]):
        output.append(string[0] + i)
    
    return output

string = input()
ans = subsequences(string)
for ele in ans:
    print(ele)


# def subsequence(str):
#     # base case
#     if len(str) == 0:
#         return [""]

#     output = []
#     for i in subsequence(str[1:]):
#         output.append(i)

#     for i in subsequence(str[1:]):
#         output.append(str[0] + i)
        
#     return output

# str = input()
# print(subsequence(str))
# print(len(subsequence(str)))