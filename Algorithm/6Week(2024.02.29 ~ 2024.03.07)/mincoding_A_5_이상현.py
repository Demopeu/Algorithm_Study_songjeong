T = int(input())

for tc in range(T):
    N = int(input())
    tree_list = sorted(map(int, input().split()))
    dist_list = [tree_list[-1] - tree for tree in tree_list]
    cnt = [0, 0]

    for dist in dist_list:
        cnt[1] += dist // 2
        cnt[0] += dist % 2

    while cnt[0] + 1 < cnt[1]:
        cnt[1] -= 1
        cnt[0] += 2

    if cnt[0] > cnt[1]:
        result = 2 * cnt[0] - 1
    else:
        result = 2 * cnt[1]

    print(f'#{tc + 1} {result}')