import sys,heapq
input = sys.stdin.readline

def Dijksta(start):
    quque = []
    heapq.heappush(quque,[matrix[start[0]][start[1]],start[0],start[1]])
    # 최저값 뽑기
    visited = [[float('inf')]*N for _ in range(N)]
    visited[start[0]][start[1]] = matrix[start[0]][start[1]]
    while quque:
        sum_number,x,y = heapq.heappop(quque)       # 순서 주의
        if x== N-1 and y == N-1:
            return sum_number
        for l in range(4):
            nx = x + dx[l]
            ny = y + dy[l]
            if 0<=nx<N and 0<=ny<N:                 # 변수로 묶는게 효율적
                if visited[nx][ny] > sum_number+matrix[nx][ny]:
                    visited[nx][ny] = sum_number+matrix[nx][ny]
                    heapq.heappush(quque,[sum_number+matrix[nx][ny],nx,ny])


test_case = 0
while True:
    test_case+=1
    N = int(input())
    if N == 0:
        break
    matrix = list(list(map(int,input().split()))for _ in range(N))
    # 좌표 설정
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    print(f'Problem {test_case}: {Dijksta((0,0))}')

# https://www.acmicpc.net/submit/4485
# 이 코드의 시간 복잡도는 O(NlogN) - while은 안치고