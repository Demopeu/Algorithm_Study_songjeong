N = int(input())
all_list = [list(map(int,input().split()) )for i in range(N)]
lst = [0]*(N+1)
# 뒤에서부터 함
for i in range(N-1,-1,-1):
    # lst에 그시절 최댓값들을 저장하는 방식을 이용
    day,money = all_list[i]
    if i+day>N:
        lst[i] = lst[i+1]
    else:
        lst[i] = max(lst[i+1],lst[i+day]+money)
print(lst[0])

# https://www.acmicpc.net/problem/14501
# 이 코드의 시간복잡도는 O(N)

from collections import deque

def bfs(start):
    q = deque()
    q.append((start, 0))
    
    while q:
        vertex, benefit = q.popleft()

N = int(input())
list_ = [list(map(int, input().split())) for _ in range(N)]
max_ = 0

for i in range(N):
    bfs()

'''
N = int(input())
all_list = {i:list(map(int,input().split()) )for i in range(1,N+1)}
lst = [0]*(N+1)
for i in range(N,0,-1):
    day,money = all_list[i]
    if i+day-1 > N:
        continue
    if money > sum(lst[i:i+day]):
        for j in range(i,i+day):
            lst[j] = 0
        lst[i] = money
print(sum(lst))

처음에 한 코드 마지막에 sum(lst) 하면 테케는 통과했는데 어디선가 틀렸음
5
2 3
2 5
3 4
1 1
1 2

부분에서 내 코드는 5인데 이부분에서는 3일차 4때문에 뒤가 다 날아가버려서
정답이 5가 나옴
정답은 2일차에 5, 4일차에 1, 5일차에 2해서 8임
'''



