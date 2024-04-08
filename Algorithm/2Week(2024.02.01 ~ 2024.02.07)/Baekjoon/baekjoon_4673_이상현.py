# 백준 4673번 셀프 넘버

# 0부터 10000까지 셀프넘버 여부를 체크하기 위한 리스트 생성
# temp[num]이 1이면 num은 셀프넘버, 0이면 셀프넘버가 아님
temp = [1] * 10001

# 셀프넘버가 아니면 생성자가 존재함. 따라서 0부터 10000까지 각 숫자가
# 생성하는 수를 체크하여 temp의 값을 0으로 바꿔줌.
for num in range(10001):
    sum_ = num + sum(int(n) for n in str(num))

    if sum_ <= 10000:
        temp[sum_] = 0

# temp 리스트에서 값이 1(셀프 넘버)인 인덱스를 출력
print(*(num for num in range(10001) if temp[num]), sep = '\n')

# https://www.acmicpc.net/problem/4673