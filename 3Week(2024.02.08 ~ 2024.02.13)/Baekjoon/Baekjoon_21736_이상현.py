import sys
sys.setrecursionlimit(1000000)

# 백준 21736번 헌내기는 친구가 필요해

count = 0

def dfs(x, y, n, m, temp):
    global count

    if not (0 <= x < n and 0 <= y < m):
        return False
    
    if not temp[x][y] == 'X':
        if temp[x][y] == 'P':
            count += 1

        temp[x][y] = 'X'
        dfs(x+1, y, n, m, temp)
        dfs(x-1, y, n, m, temp)
        dfs(x, y+1, n, m, temp)
        dfs(x, y-1, n, m, temp)
        return True
    
    return False

n, m = map(int, input().split())
temp = []
x, y = 0, 0

for i in range(n):
    temp.append(list(input()))

for i in range(n):
    for j in range(m):
        if temp[i][j] == 'I':
            x, y = i, j
            break
    if x:
        break

dfs(x, y, n, m, temp)
print(count if count else 'TT')

# 링크 : https://www.acmicpc.net/problem/21736