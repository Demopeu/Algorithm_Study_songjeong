# Python 시간 초과
# C++로 변환하면 Pass

def dfs(cnt, num, score):
    global max_

    if cnt == N:
        max_ = max(max_, score)

    for i in range(1, N + 1):
        if not visited[i]:
            visited[i] = True
            left = i - 1
            right = i + 1

            while visited[left]:
                left -= 1

            while visited[right]:
                right += 1

            if left == 0 and right == N + 1:
                dfs(cnt + 1, i, score + score_list[i])
                visited[i] = False
            else:
                dfs(cnt + 1, i, score + score_list[left] * score_list[right])
                visited[i] = False

T = int(input())

for tc in range(T):
    N = int(input())
    score_list = [1] + list(map(int, input().split())) + [1]
    visited = [False] * (N + 2)
    max_ = 0
    len_ = len(score_list)

    if len_ > 3:
        visited[1] = True
        dfs(1, 1, score_list[2])
        visited[1] = False

        for num in range(2, N):
            visited[num] = True
            dfs(1, num, score_list[num - 1] * score_list[num + 1])
            visited[num] = False

        visited[N] = True
        dfs(1, N, score_list[N - 1])
        visited[N] = False
    else:
        max_ = score_list[1]

    print(f'#{tc + 1} {max_}')