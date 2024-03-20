# https://www.acmicpc.net/problem/4485

# 우선순위 큐 사용
import heapq

# '그 방향'
dx = [0,1,0,-1]
dy = [-1,0,1,0]

# 테스트 케이스 번호
test_case = 0
while True:
    # 테스트 케이스 번호 추가
    test_case += 1
    # 동굴 너비
    N = int(input())
    # 0이면 입력 종료
    if not N:
        break
    
    # 동굴
    MAP = [list(map(int,input().split())) for _ in range(N)]
    # 구역별 최소 손해
    visited = [[float('inf')]*N for _ in range(N)]
    # 생각해보니 그냥 방문 여부로 해도 될것 같다
    # 우선순위 큐로 했을 때 손해가 적은걸 먼저 적용한다면
    # 똑같은 비용이 더해지니까 먼저 오는거보다 작아질 수 없다
    # visited = [[0] * N for _ in range(N)]

    # 시작점의 현재 잃은 루피,x,y
    hq = [(MAP[0][0],0,0)]
    # 시작점 손해
    visited[0][0] = MAP[0][0]

    while hq:
        # 잃은 루피,x,y
        lost,x,y = heapq.heappop(hq)
        # 목적지에 도착하면 종료(lost에 목적지의 최소 비용 저장)
        if x == N-1 and y == N-1:
            break
        
        # 상하좌우 순회
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위 안일 경우
            if 0 <= nx < N and 0 <= ny < N:
                # 현재의 최소 손해보다 작으면 갱신하고 큐에 추가
                if visited[ny][nx] > lost + MAP[ny][nx]:
                    visited[ny][nx] = lost + MAP[ny][nx]
                    heapq.heappush(hq,(visited[ny][nx],nx,ny))
                # 방문여부로 했을 때
                # if not visited[ny][nx]:
                #     visited[ny][nx] = 1
                #     heapq.heappush(hq, (lost + MAP[ny][nx], nx, ny))

    print(f'Problem {test_case}: {lost}')
