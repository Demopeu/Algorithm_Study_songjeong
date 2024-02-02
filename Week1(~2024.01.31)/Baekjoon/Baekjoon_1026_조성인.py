N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

# 함수 S 정의
def S(new_A):
    result = 0
    for i in range(N):
        result += new_A[i] * B[i]
    return result

# 곱의 합을 최솟값으로 받으려면 큰수와 작은수의 곱으로 재배열
# B는 재배열하면 안되니 B의 복사본을 만들어서 사용
B_ = B[:]
B_.sort()

# B_에 매핑되게 A는 역순으로 재배열
A.sort(reverse=True)
# B의 인덱스 리스트 생성
index_list = []

for i in range(N):
    idx = B_.index(B[i])

    # 이미 인덱스에 있으면 +1
    while idx in index_list:
        idx += 1

    index_list.append(idx)

# A에 B 크기에 맞게 재배열
A = [A[idx] for idx in index_list]

print(S(A))