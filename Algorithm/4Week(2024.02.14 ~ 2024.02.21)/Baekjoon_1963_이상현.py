# 백준 1963번 소수 경로5

from collections import deque

# 두 소수가 주어지면 한 개의 소수에서 다른 소수로
# 바꾸는 데에 필요환 변경 횟수를 구하는 문제

# 변경할 때마다 한 자리 수만 바꿀 수 있고, 변경된 수
# 또한 소수여야 함

# 문제에서 네자리 수만 주어진다고 했으므로
# 9999까지 소수 여부를 미리 판단
prime = [0, 0, 1] + [1] * 9997


# 에라토스테네스의 체 사용
for n in range(2, 10000):
    if prime[n]:
        for i in range(2 * n, 10000, n):
            prime[i] = 0

def bfs(start):
    q = deque()
    q.append((start, 0))
    visited = [0] * 10000
    visited[start] = 1

    while q:
        # num은 현재 수, cnt는 현재까지 변경 횟수
        num, cnt = q.popleft()

        # 네 자리 수가 아닐시 다음으로 넘어감
        if not (1000 <= num < 10000):
            continue

        # 우리가 찾는 목표라면 반복문 종료
        if num == end:
            break

        # 각 자리 수를 변경하여 그 수가 소수라면 탐색
        for i in range(10):
            for next_num in [num - num % 10 + i, num - ((num % 100) // 10) * 10 + i * 10,
                             num - ((num // 100) % 10) * 100 + i * 100, num - (num // 1000) * 1000 + i * 1000]:
                if not visited[next_num] and prime[next_num]:
                    q.append((next_num, cnt + 1))
                    visited[next_num] = 1

    # 만약 모든 경우를 탐색하여 두 소수 사이에 변환이 존재하면
    # 변환 횟수를, 존재하지 않는다면 Impossible 반환 후 출력
    return cnt if num == end else 'Impossible'

for _ in range(int(input())):
    start, end = map(int, input().split())
    print(bfs(start))

# 문제링크 : https://www.acmicpc.net/problem/1963
# 시간복잡도 : O(V + E)
# 34052 KB, 88 ms