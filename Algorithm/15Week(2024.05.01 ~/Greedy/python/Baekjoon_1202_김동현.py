import heapq,sys
input = sys.stdin.readline

N,K = map(int,input().split())
bosuck = sorted(list(map(int,input().split()))for _ in range(N))
bag = sorted(list(int(input()) for _ in range(K)))
answer = 0
used_bosuck = []
for i in bag:
    while bosuck and bosuck[0][0] <= i:
        heapq.heappush(used_bosuck,-bosuck[0][1])
        heapq.heappop(bosuck)
    if used_bosuck:
        answer -= heapq.heappop(used_bosuck)
print(answer)

# https://www.acmicpc.net/problem/1202
# 파이썬 재활의 일환