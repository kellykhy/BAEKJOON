# 백준 9251번 LCS

import sys
input = sys.stdin.readline

str1 = input().rstrip()
str2 = input().rstrip()

table = [[0 for _ in range(len(str2)+1)] for _ in range(len(str1)+1)]

for i in range(1, len(str1)+1):
    for j in range(1, len(str2)+1):
        if str1[i-1] == str2[j-1]:
            table[i][j] = table[i-1][j-1] + 1
        else:
            table[i][j] = max(table[i-1][j], table[i][j-1])
print(table[len(str1)][len(str2)])