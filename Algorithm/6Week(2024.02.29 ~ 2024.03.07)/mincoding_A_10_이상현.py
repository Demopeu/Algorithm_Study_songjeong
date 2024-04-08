from collections import deque

def topological_sort():
    q = deque()
    result = time_table[:]

    for i in range(1, N + 1):
        if not indegree[i]:
            q.append(i)

    while q:
        current_work = q.popleft()

        for work in graph[current_work]:
            result[work] = max(result[work], result[current_work] + time_table[work])
            indegree[work] -= 1

            if not indegree[work]:
                q.append(work)

    return result

T = int(input())

for tc in range(T):
    N = int(input())
    time_table = [0] * (N + 1)
    graph = [[] for _ in range(N + 1)]
    indegree = [0] * (N + 1)
    min_ = 10 ** 8

    for i in range(N):
        time_, num, *list_ = map(int, input().split())
        time_table[i + 1] = time_

        for elem in list_:
            graph[elem].append(i + 1)
            indegree[i + 1] += 1

    temp_degree = indegree[:]
    temp_time = time_table[:]

    for i in range(1, N + 1):
        time_table[i] //= 2
        result = topological_sort()

        if any(indegree[j] for j in range(1, N + 1)):
            continue

        min_ = min(min_, max(result))

        indegree = temp_degree[:]
        time_table = temp_time[:]

    print(f'#{tc + 1} {min_ if min_ != 10 ** 8 else -1}')