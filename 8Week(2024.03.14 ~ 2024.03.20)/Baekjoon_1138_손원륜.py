T = int(input())

lst = list(map(int, input().split()))
ans = [0] * T       # T만큼 빈 리스트 생성

print(lst)

for i in range(T):
    cnt = 0
    for j in range(T):
        if cnt == lst[i] and ans[j] == 0:
            ans[j] = i + 1
            break
        elif ans[j] == 0:
            cnt += 1

print(*ans, end=' ')    # 언패킹해야 대괄호 빠짐

