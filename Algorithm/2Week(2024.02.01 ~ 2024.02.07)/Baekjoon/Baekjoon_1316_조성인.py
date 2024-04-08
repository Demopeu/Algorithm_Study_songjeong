# https://www.acmicpc.net/problem/1316

# 시간 복잡도 : O(NL)

N = int(input())
words = [input() for _ in range(N)]

# 그룹단어의 수
count = 0

# 그룹단어의 조건 : 같은 문자는 연속해서 배열되어야 함
# 반대로 같은 문자 사이에 다른 문자가 있으면 그룹단어가 아니게 됨 -> 길이가 3 미만이면 그룹단어가 아닐 수가 없음

for word in words:
    # 단어의 길이가 3미만일 경우 무조건 그룹단어
    if len(word) < 3:
        # 그룹단어 +1
        count += 1
        # 다음 단어로 넘어감
        continue
    else:
        # 그룹단어의 조건이 여부가 갈리는 3번째 문자부터 순회
        for i in range(2, len(word)):
            # 문자가 앞의 문자와 일치하지 않고, 앞에 해당 문자가 존재하였으면 반복문을 종료
            if word[i] != word[i-1] and word[i] in word[:i]:
                break
            else:
                # 마지막 문자까지 해당사항이 없었을 경우
                if i == len(word)-1:
                    # 그룹단어 +1
                    count += 1

print(count)