# 2개의 리스트를 입력받아 각 리스트의 수를 곱한 결과를
# 모두 더한 값의 최솟값을 구하는 문제

N = int(input())

# a는 작은 순으로, b는 큰 순서대로 정렬
a_list = sorted(list(map(int, input().split())), reverse = True)
b_list = sorted(list(map(int, input().split())))

sum_ = 0

# sigma(a의 최소값 * b의 최대값)
for index in range(N):
    sum_ += a_list[index] * b_list[index]

print(sum_)