t = int(input())

for tc in range(1, t + 1):
    n = int(input())        # 나무의 개수
    trees = list(map(int, input().split()))     # 나무 높이
    max_high = max(trees)   # 최대 높이
    cnt_lst = [0 for _ in range(3)]
    day = 0

    for tree in trees:
        diff = max_high - tree
        if diff and diff % 2 == 1:
            cnt_lst[1] += 1
            cnt_lst[2] += int((diff - 1) // 2)
        elif diff and diff % 2 == 0:
            cnt_lst[2] += int(diff // 2)

    while cnt_lst[1] > 0 or cnt_lst[2] > 0:
        day += 1

        if day % 2 == 1:
            if cnt_lst[1] > 0 and cnt_lst[2] > 1:           # 1일 개수 1 이상이고, 2일 개수 1 이상이면 1씩 소비
                cnt_lst[1] -= 1
            elif cnt_lst[1] > 0:                            # 1일 개수 0 이상이면, 1일 1씩 소비
                cnt_lst[1] -= 1
            elif cnt_lst[1] == 0 and cnt_lst[2] > 1:        # 1일 개수 0이고, 2일 개수 1 이상이면, 2일를 땡겨서 1씩 소비
                cnt_lst[2] -= 1
                cnt_lst[1] += 1
            elif cnt_lst[1] == 0 and cnt_lst[2] == 1:       # 2일 개수 1개라면, 다음날 종료 가능하기에 continue
                continue
        elif day % 2 == 0:
            if cnt_lst[2] > 0:
                cnt_lst[2] -= 1

    print(f'#{tc} {day}')
