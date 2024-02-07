# https://www.acmicpc.net/problem/2563

# 시간 복잡도 : O(N)

# 색종이 수는 100 이하
# 색종이가 도화지밖을 나가는 경우 없음

# 직접 그리기
# 도화지
paper = [[0]*100 for i in range(100)]

N = int(input())

# 색종이 모서리 좌표
for _ in range(N):
    x,y = map(int,input().split())
    
    # 모서리 기준 색종이 넓이만큼 표시
    for i in range(10):
        for j in range(10):
            paper[x+i][y+j] = 1

# 총 넓이
r = 0
for i in paper:
    r += sum(i)
print(r)