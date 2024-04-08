# 백준 17413번 단어 뒤집기 2

# 입력받은 문자열에서 '<'은 'CLC'로, '>'은 'CRC'로 공백(' ')은 'CSC'로 바꾼 후
# 'C'를 기준으로 문자열을 나눈다.
S = input().replace('<', 'CLC').replace('>', 'CRC').replace(' ', 'CSC').split('C')
index = 0

# 나눠진 각각의 단어들마다 뒤집을지 안뒤집을지 결정을 해야 하는데
# 이를 index로 확인함. 태그가 열렸다('<') 닫히면('>') index의 값은
# 짝수이므로 index가 짝수일 때 문자열을 뒤집어줌
for i in range(len(S)):
    if S[i] == 'L' or S[i] ==  'R':
        index += 1

    if index % 2 == 0:
        S[i] = S[i][::-1]

# 문제에서 원하는 결과로 출력하기 위해 'L'은 '<', 'R'은 '>', 'S'는 ' '으로
# 바꾼 후 출력
print(''.join(S).replace('L', '<').replace('R', '>').replace('S', ' '))

# https://www.acmicpc.net/problem/17413