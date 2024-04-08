import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)  # 재귀 제한 늘이기

def dfs(x, y, cnt):
    visited[x][y] = True  # 방문했으므로 True로 변경
    if graph[x][y] == 'P':
        cnt += 1  # 현재 위치가 'P'인 경우 cnt 증가
    for i in range(4):
        nx = x + dx[i]  # 다음 위치 계산
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            if graph[nx][ny] != "X":
                cnt = dfs(nx, ny, cnt)  # 다음 위치로 이동하여 재귀적으로 dfs 호출하여 cnt 업데이트
    return cnt

dx = [0, 1, 0, -1]  # 4방향
dy = [1, 0, -1, 0]
n, m = map(int, input().split())
graph = list(input() for _ in range(n))  # 그래프 정보 입력 받기
visited = [[False] * m for _ in range(n)]  # 방문 여부를 저장할 2차원 리스트 False로 초기화

cnt = 0  # 초기화
for i in range(n):
    for j in range(m):
        if graph[i][j] == "I":  # 시작 지점인 'I'를 찾으면 dfs 함수 호출
            cnt = dfs(i, j, cnt)

if cnt == 0:  # P의 개수
    print("TT")
else:
    print(cnt)

'''
https://www.acmicpc.net/problem/21736
시간 복잡도: O(nm)
챗gpt 첨언(시간복잡도는 잘 몰라서..)
sys.setrecursionlimit(10**6): 시스템 재귀 제한을 설정하는데, O(1)의 시간 복잡도를 가집니다.
input = sys.stdin.readline: 입력을 받는데, 입력의 크기에 비례하여 O(n)의 시간 복잡도를 가집니다. (n은 입력의 크기)
dfs 함수: 재귀적으로 호출되는 함수로, 모든 지점을 한 번씩 방문하므로 O(nm)의 시간 복잡도를 가집니다. (n과 m은 그래프의 크기)
for 문: 이중 반복문이므로 O(nm)의 시간 복잡도를 가집니다.
따라서, 전체 코드의 시간 복잡도는 O(nm)입니다. 그래프의 크기에 비례하여 실행 시간이 증가합니다.
참고로, 코드 내에서 사용된 공간 복잡도는 O(nm)입니다. 그래프와 방문 여부를 저장하기 위한 2차원 리스트의 크기가 n*m이기 때문입니다.
'''