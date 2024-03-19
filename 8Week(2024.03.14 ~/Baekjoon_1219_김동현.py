import sys,collections
deque = collections.deque
input = sys.stdin.readline

# 벨만 포드 알고리즘
# https://great-park.tistory.com/134 참고함
# 매 단계마다 모든 간선을 전부 확인하면서 모든 노드간의 최단거리를 구하는 방법
# 다익스트라는 방문하지 않는 노드 중에 가장 가까운 노드만 방문
# 벨만 포드는 매 단계마다 끝까지 다 탐색해야함
# 음의 가중치를 가지는 간선이 있더라도 최적의 해를 구할 수 있음

'''
동작 과정
    1. 출발 노드 설정
    2. 최단 거리 테이블을 초기화
    3. for _ in range(V-1)에 대하여 모든 간선을 확인 후, 다른 모든 지점까지의 최단 경로를 구함
        - 벨만 포드 알고리즘은 한 노드에서 다른 노드까지의 최단 경로를 많아봐야 V-1개의 간선을 지난 다는 가정을 세우고 시작
        - 왜냐면 최단 경로가 V-1개보다 많은 간선을 지나게 된다면 음의 사이클이 존재하는다는 의미
    (4. 만약 음의 사이클이 발생하는지 알고 싶으면 3번 한번 더 실행(왜냐면 최단 거리 갱신 될 꺼기 때문)
'''


# 벨만 포드 알고리즘
def bellman(start):
    min_list[start] = money_in_city[start]
    for _ in range(N-1):
        for S, E, M in new_M_list:
            if min_list[S] != -1*sys.maxsize and min_list[E] < min_list[S]+M:
                min_list[E] = min_list[S]+M


# 도착 할 수 있는지 판별유무
def find_goal(start):
    quque = deque([start])
    visited = [False]*N
    visited[start] = True
    while quque:
        node = quque.popleft()
        if node == end_city:
            return True
        for S,E,M in new_M_list:
            if S == node and not visited[E]:
                visited[E] = True
                quque.append(E)
    return False


# 음의 사이클을 찾기
def find_negative_cycle():
    for S,E,M in new_M_list:
        if min_list[S] != -1*sys.maxsize and min_list[E] < min_list[S]+M:
            if find_goal(S):
                return False
    return True


# 함수 받기
N,start_city,end_city,M = map(int,input().split())

# 차례대로 시작도시, 끝도시, 교통수단 비용
M_list = list(list(map(int,input().split())) for _ in range(M))
money_in_city = list(map(int,input().split()))
min_list = [-1*sys.maxsize]*N
new_M_list = []

# 도시에 도착했을 때, 벌 돈과 교통수단 비용을 뺀 가격
for i in M_list:
    S,E,M = i
    M = money_in_city[E]-M
    new_M_list.append((S, E, M))

# min_list 갱신
bellman(start_city)
# 음의 사이클 확인(하지만 그 사이클 중에 도착할 수 있는 경로가 있으면 False)
answer_negative_cycle = find_negative_cycle()

# 체크
# print('음의사이클:',answer_negative_cycle)
# print(min_list)

# 정답 호출
if min_list[end_city] == -1*sys.maxsize:
    print('gg')
else:
    # 사이클이 있는 경우
    if not answer_negative_cycle:
        print('Gee')
    else:
        print(min_list[end_city])
'''
첫번째 코드

# 벨만 포드 알고리즘
def bellman(start_city):
    min_list[start_city] = money_in_city[start_city]
    for find_negative_cycle in range(N-1):
        for S,E,M in new_M_list:
            if min_list[S] != -1*sys.maxsize and min_list[E] < min_list[S]+M:
                min_list[E] = min_list[S]+M
                if find_negative_cycle == N-1:
                    return (False,new_min_list)
        if find_negative_cycle == N-2:
             new_min_list= min_list
    return (True,new_min_list)
    
N,start_city,end_city,M = map(int,input().split())
# 차례대로 시작도시, 끝도시, 교통수단 비용
M_list = list(list(map(int,input().split())) for _ in range(M))
money_in_city = list(map(int,input().split()))
min_list = [-1*sys.maxsize]*N
new_M_list = []
# 도시에 도착했을 때, 벌 돈과 교통수단 비용을 뺀 가격
for i in M_list:
    S,E,M = i
    M = money_in_city[E]-M
    new_M_list.append((S,E,M))

if start_city == end_city:
    print(money_in_city[end_city])
else:
    answer = bellman(start_city)
    if answer[1][end_city] == -1*sys.maxsize:
        print('gg')
    else:
        if answer[0]:
            print(answer[1][end_city])
        else:
            print('Gee')
            
첫번째 코드의 문제점은 min_list가 갱신 되버려서 12%에서 실패
그리고 음의 사이클이 있음에도 불구하고 도착 도시에 갈 수 있기 때문에 Gee이 아닌 결과를 표시해야함
반례 코드
1 0 0 2
0 0 0
0 0 7
6
정답은 6

반례 코드
4 0 3 4
0 1 0
0 3 5
1 2 0
2 1 0
0 5 5 10
정답은 5
'''

# https://www.acmicpc.net/problem/1219
# 이 코드의 시간 복잡도는 O(N^2)
# 벨만 포드 알고리즘의 경우 O(VE)
# 비슷한 알고리즘으로 플로이드-워셜 알고리즘은 O(N^3)
# 걍 노가다 = 플로이드-워셜 알고리즘