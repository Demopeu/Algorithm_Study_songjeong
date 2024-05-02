def change(number):
    answer = ''
    while number > 0:
        answer = str(number % k) + answer
        number //= k
    return answer


n,k = map(int,input().split())
print(change(sum(int(i) for i in change(n).split('0') if i !='')))

# https://www.acmicpc.net/problem/25371
# 파이썬 재활의 일환

