# https://www.acmicpc.net/problem/1446

N, D = map(int,input().split())

# 도로 정보
roads = []
for _ in range(N):
    start,end,distance = map(int,input().split())
    # 도로에 추가되는 조건
    # 목적지보다 멀리가지 않을것(역주행 불가이므로)
    # 지름길이 더 멀지 않을 것
    if end <= D and end - start > distance:
        roads.append([start,end,distance])

# 도착지점을 기준으로 정렬
roads.sort(key=lambda x:x[1])
# 거리별 최소 이동 거리
min_root = [n for n in range(D+1)]

# 지름길 순회
for i in range(len(roads)):
    # 도착지점까지의 최소거리 비교
    # 현재의 최소거리와 지름길을 이용했을때의 거리를 비교해서 저장
    min_root[roads[i][1]] = min(min_root[roads[i][0]] + roads[i][2],min_root[roads[i][1]])
    # 그리고 그 이후의 거리 재계산
    for j in range(roads[i][1]+1,D+1):
        min_root[j] = min_root[j-1] + 1

# D에 도달하는 최소 거리 출력
print(min_root[D])