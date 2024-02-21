from collections import deque

def bfs(x, y, matrix, visit):
    queue = deque()
    queue.append((x, y))
    visit[x][y] = 1
    v_cnt = 0       # visit_cnt 선언 및 0 초기화

    while queue:
        v_cnt += 1
        temp = deque()      # 임시 queue 선언
        for q in queue:     # queue 끝까지 반복문 돌면서 다음 depth만 temp에 추가
            x, y = q[0], q[1]
            if visit[x][y] == 1 and x == n - 1 and y == m - 1:      # 도착점에 도착하면 return v_cnt
                return v_cnt
            else:                   # queue 요소 하나가 갈 수 있는 길 탐색
                for i in range(4):
                    temp_x = x + dx[i]
                    temp_y = y + dy[i]
                    if temp_x < 0 or temp_x >= n or temp_y < 0 or temp_y >= m:
                        continue
                    elif visit[temp_x][temp_y] == 1 or matrix[temp_x][temp_y] == 0:
                        continue
                    else:
                        temp.append((temp_x, temp_y))       # 같은 depth 요소들만 temp에 추가
                        visit[temp_x][temp_y] = 1           # 시간 초과 문제로 append하면서 visit 체크
                queue = temp        # queue에 temp 할당함으로써 while문 지속 가능
    return 0    # 도착점에 도착 못할 시 return 0


n, m = map(int, input().split())
maze = [list(map(int, list(input()))) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
result = bfs(0, 0, maze, visited)

print(result)


# 시간복잡도: O(NM)
# 출처: https://www.acmicpc.net/problem/2178