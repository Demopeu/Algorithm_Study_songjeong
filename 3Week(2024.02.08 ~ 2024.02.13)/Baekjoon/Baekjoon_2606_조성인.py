# https://www.acmicpc.net/problem/2606

# 시간복잡도 : O(N * M)

# 컴퓨터 전체 수
N = int(input())
# 네트워크 경로 수
M = int(input())

# 네트워크
connect = [list(map(int,input().split())) for _ in range(M)]

# 감염된 컴퓨터
infection = [1]
# 방문한 네트워크 경로
visited = []

# 감염된 컴퓨터를 순회(처음에는 1뿐이지만 나중에 추가되면 더 돌아감)
for inf in infection:
    # 네트워크를 순회
    for con in connect:
        # 네트워크 순회 중 이미 방문한 경로면 지나감
        if con in visited:
            continue
        else:
            # 감염된 컴퓨터가 있으면
            if con[0] == inf:
                # 방문 경로에 추가하고
                visited.append(con)
                # 상대방이 감염되지 않은 컴퓨터라면
                if con[1] not in infection:
                    # 감염
                    infection.append(con[1])
            # 양방향 고려
            elif con[1] == inf:
                visited.append(con)
                if con[0] not in infection:
                    infection.append(con[0])

# 1번을 제외한 수를 세야해서 인덱스 0번에 위치한 1번 컴퓨터를 제거 후 개수 세기
infection.pop(0)

print(len(infection))