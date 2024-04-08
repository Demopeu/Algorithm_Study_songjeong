# 재귀 함수를 이용한 dfs 할 경우 필요해서 넣음
# import sys
# sys.setrecursionlimit(10**6)

# dfs 함수
def dfs(dohyun):
    stack = list()                                                             # 노란 줄이 싫었어
    stack.append(dohyun)                                                        # 보기 편하라고 2줄
    friend = 0                                                                 # 친구를 만나는 함수

    visited[dohyun[0]][dohyun[1]] = True

    while stack:
        node = stack.pop()
        x, y = node[0], node[1]

        for l in range(4):                                                      # 상하좌우 전부 탐색
            new_i = x +dx[l]
            new_j = y +dy[l]

            if 0 <= new_i < N and 0 <= new_j < M and not visited[new_i][new_j]:       # 캠퍼스 내에 둘러보지 않은 곳
                if matrix[new_i][new_j] == 'P':
                    friend += 1                                                 # 사람 만나면 친구 +1
                if matrix[new_i][new_j] != 'X':                                 # 벽만 아니면 stack에 추가
                    visited[new_i][new_j] = True
                    stack.append((new_i,new_j))
                    
    return friend


# 재귀 함수를 이용한 dfs
'''
def dfs(node):
    global friend
    x, y = node[0], node[1]
    visited[x][y] = True
    
    if matrix[x][y] == 'P':
        friend += 1

    for l in range(4):
        new_i = x + dx[l]
        new_j = y + dy[l]

        if 0 <= new_i < N and 0 <= new_j < M and not visited[new_i][new_j]:
            if matrix[new_i][new_j] != 'X':
                dfs((new_i,new_j))
'''

# 변수 생성
N, M = map(int,input().split())
matrix = [input() for _ in range(N)]                # 캠버스 생성
visited = [[False]*M for _ in range(N)]             # 방문 체크
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# 재귀 함수 global 지정을 위한 함수
# friend = 0

# 도연이 찾기
for i in range(N):
    flag = False
    for j in range(M):
        if matrix[i][j] == 'I':
            start = (i,j)
            flag = True
            break
    if flag:                                # 간단한 백트래킹
        break

# 함수를 돌리고 정답 찾기
answer = dfs(start)
print(answer if answer > 0 else 'TT')


# 재귀 함수를 이용한 dfs 구문
'''
dfs(start)
print(friend if friend > 0 else print('TT'))
'''

# 이 코드의 시간 복잡도는 O(N*M)
    # 각 노드마다 상하좌우를 확인하므로 O(N*M)
    # dfs 함수 호출이 상수의 시간이 소요되므로 큰 영향을 주지 않음

# 항상 두가지 방법으로 풀어 놓지만, 재귀함수를 이용한 dfs는 효율이 너무 별루임
    # 실제로 while문을 사용한 dfs가 메모리, 시간 절반임
    # N,M이 작으면 상관 없지만, 크면 클 수록 재귀문은 효율이 떨어짐