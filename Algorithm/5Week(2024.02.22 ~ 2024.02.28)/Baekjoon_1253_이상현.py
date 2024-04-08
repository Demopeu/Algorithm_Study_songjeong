# 백준 1253번 좋다

# 주어진 수 중에서 다른 두 수의 합으로 나타낼 수 있는 수의 개수를 구하는 문제
N = int(input())
# 입력받을 때 정렬
num_list = sorted(map(int, input().split()))
cnt = 0

for i, num in enumerate(num_list):
    # 자기 자신은 합의 표현으로 나타내는데 사용할 수 없음
    # 투 포인터 이용
    list_ = num_list[:i] + num_list[i + 1:]
    left = 0
    right = N - 2

    while left < right:
        # 현재 두 포인터가 가르키는 값의 합을 temp에 저장
        temp = list_[left] + list_[right]

        # 두 수의 합이 num과 같으면 cnt를 1 증가
        if temp == num:
            cnt += 1
            break

        # temp가 num보다 크면 합을 작게 해야하므로
        # right를 1 감소, 작을 경우 합을 크게 해야하므로
        # left를 1 증가
        elif temp > num:
            right -= 1

        else:
            left += 1

print(cnt)

# 시간 복잡도 : O(N ** 2)
# 문제 링크 : https://www.acmicpc.net/problem/1253