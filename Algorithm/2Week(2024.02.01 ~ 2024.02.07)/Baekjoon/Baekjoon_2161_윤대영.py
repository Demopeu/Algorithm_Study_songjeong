n = int(input())
lst = list(range(1, n + 1))     # 1부터 n까지의 리스트 선언

while len(lst) > 1:
    print(lst.pop(0), end=' ')  # pop 메소드는 요소 위치 삭제 후 삭제한 값 반환
    lst.append(lst.pop(0))

print(*lst)

# 시간 복잡도: O(n)
# 출처: https://www.acmicpc.net/problem/2161
