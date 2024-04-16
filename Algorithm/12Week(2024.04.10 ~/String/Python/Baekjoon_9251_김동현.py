import sys
input = sys.stdin.readline
a = ' '+input().rstrip()
b = ' '+input().rstrip()
lcs = list([0]*len(b) for _ in range(len(a)))
for i in range(1,len(a)):
    for j in range(1,len(b)):
        if a[i]==b[j]:
            lcs[i][j] = lcs[i-1][j-1]+1
        else:
            lcs[i][j] = max(lcs[i][j - 1],lcs[i-1][j])
print(lcs[-1][-1])

# https://www.acmicpc.net/problem/9251
