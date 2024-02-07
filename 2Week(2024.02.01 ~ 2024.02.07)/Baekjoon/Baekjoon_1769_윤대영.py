x = input()
y = x
cnt = 0             # 문제 변환 횟수

while len(y) > 1:
    temp = 0        # 각 자리수의 합 넣을 임시 변수
    for digit in y: # 문자열로 변환한 y를 한자리씩 반복
        temp += int(digit)
    y = str(temp)   # 각 자리수의 합을 문자열로 변환하여 y에 재할당
    cnt += 1

print(cnt)
if int(y) % 3 == 0:
    print('YES')  
else:
    print('NO')

# 시간 복잡도: O(log10(x))
# 출처: https://www.acmicpc.net/problem/1769