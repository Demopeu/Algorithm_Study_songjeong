import sys,copy
input = sys.stdin.readline

def find_set(x):
    while parents[x] != x:
        x = parents[x]
    return x


def union_set(x,y):
    x = find_set(x)
    y = find_set(y)
    if x==y:
        return
    if x<y:
        parents[y] = x
    else:
        parents[x] = y


N = int(input())
parents = [i for i in range(N)]
planets = []
distances = []
sum_distance = 0

for i in range(N):
    x,y,z = map(int,input().split())
    planets.append([i,x,y,z])

planets_x = sorted(copy.deepcopy(planets),key=lambda x:x[1])
planets_y = sorted(copy.deepcopy(planets),key=lambda x:x[2])
planets_z = sorted(copy.deepcopy(planets),key=lambda x:x[3])

for i in range(N-1):
    distances.append((abs(planets_x[i][1]-planets_x[i+1][1]),planets_x[i][0],planets_x[i+1][0]))
    distances.append((abs(planets_y[i][2]-planets_y[i+1][2]),planets_y[i][0],planets_y[i+1][0]))
    distances.append((abs(planets_z[i][3]-planets_z[i+1][3]),planets_z[i][0],planets_z[i+1][0]))

distances.sort()
for distance,planet1,planet2 in distances:
    planet1 = find_set(planet1)
    planet2 = find_set(planet2)
    if planet1 == planet2:
        continue
    union_set(planet1,planet2)
    sum_distance += distance
print(sum_distance)


# https://www.acmicpc.net/problem/2887
# 시간 복잡도는 O(Nlog(N))
# 각 행성을 x,y,z에 따라 정렬하는 부분이 O(Nlog(N))
# 거리 저장하는데 O(N)
# 크루스칼 알고리즘 O(log(N))
# 따라서 O(N log N)


'''
메모리 초과
가능한 모든 간선을 다 저장하다 보니 N*(N-1)/2 만큼의 간선 저장

for i in range(N):
    for j in range(i+1,N):
        x,y,z=planets[i]
        x1,y1,z1 = planets[j]
        money.append((i,j,(min(abs(x-x1),abs(y-y1),abs(z-z1)))))

money.sort(key=lambda x:x[2])

# 시간 복잡도
위 처럼 구현 할 경우 O(N^2))
시간 제한 1초 임에도 행성 개수인 N개가 100,000이므로
N^2 == 100만 -> 따라서 100초 걸림
O(N*log(N)) == 50만 --> 0.5초 걸림

# 메모리 초과
128mb 1600만개의 int를 사용할 수 있음
C++ 기준으로 1억개의 연산을 진행할 수 있음
그래서 데이터의 크기가 1만개를 초과할 경우 N**2 = 1억
1만개를 초과하면 의심해보자

따라서, 1억개 연산 당 1초 and 128mb라고 생각하면 편하다
'''