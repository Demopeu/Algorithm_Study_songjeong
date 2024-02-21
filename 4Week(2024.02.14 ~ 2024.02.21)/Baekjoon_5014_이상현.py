# 백준 5014번 스타트링크

from collections import deque

# S층에서 G층으로 가기 위해 눌러야 하는 버튼의 최솟값을 구하는 문제
def bfs(start):
    q = deque()
    q.append((start, 0))
    visited = [0] * (floor + 1)
    visited[start] = 1
    cnt = 0

    while q:
        # pos는 현재 층, cnt는 현재까지 누른 버튼의 횟수
        pos, cnt = q.popleft()

        # 목표 층수에 도달했다면 반복문 종료
        if pos == end:
            return cnt

        # up 버튼을 눌렀을 때는 위로
        # down 버튼을 눌렀을 때는 아래로
        # 방문하지 않았다면 방문처리 후 cnt를 1 증가시키고 탐색
        for move in [up, -down]:
            if 0 < pos + move <= floor and not visited[pos + move]:
                q.append((pos + move, cnt + 1))
                visited[pos + move] = 1

    # 목표 층수에 도달하지 못하고 반복문이 종료됐다면
    # 'use the stairs'라는 문구를 반환
    return 'use the stairs'

floor, start, end, up, down = map(int, input().split())
print(bfs(start))

# 문제링크 : https://www.acmicpc.net/problem/5014
# 시간복잡도 : O(floor)
# 40296 KB, 448 ms Python 3