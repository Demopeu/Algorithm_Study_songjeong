# https://www.acmicpc.net/problem/7795

# 테스트 케이스의 개수
T = int(input())
for test_case in range(1,T+1):
    # A,B의 길이
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    
    # 이분 탐색을 돌릴 B 정렬
    B.sort()
    # 쌍의 개수
    count = 0
    
    # A를 순회
    for a in A:
        # B 범위의 시작과 끝
        start = 0
        end = M - 1
        
        while start <= end:
            # 중간
            mid = (start + end) // 2
            
            # B의 중간 인덱스보다 a가 작거나 같으면
            if a <= B[mid]:
                # 인덱스를 땡김
                end = mid - 1
            # a가 더 크면
            else:
                # 그 뒤를 시작으로 잡음
                start = mid + 1
        
        # 이렇게 하면 a보다 작은 값들은 인덱스 start의 앞에 모이게 됨
        # 그러면 start == len(B[0:start-1])이므로 이걸 카운트함
        count += start
    
    # 그렇게 모은 숫자를 출력
    print(count)