N = int(input())
# 메모리제이션 이용
# 피보나치 마냥 끝없이 사용하면 무조건 에러남 0.15초 제한
memory = [0]*(N+1)
# memory[1] 은 1이 1이 되기 위한 횟수이므로 생략
for i in range(2,N+1):
    # -1 하는 방법
    memory[i] = memory[i-1] + 1
    if i%2 == 0:
        # 만약 4이면 2의 횟수를 찾아 +1 만 하면 횟수 저장 됨
        memory[i] = min(memory[i],memory[i//2]+1)
    if i%3 == 0:
        memory[i] = min(memory[i],memory[i//3]+1)

print(memory[N])

# https://www.acmicpc.net/problem/1463
# 이 코드의 시간복잡도는 O(N)
# for 구문 N
# 처음에는 하향식으로 하려 했는데 그러면 10 -> 9 -> 3 -> 1 이부분이 해결 불가능
