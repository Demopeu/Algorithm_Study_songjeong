T = int(input())

# 리스트 내 요소가 연결되었는지 확인하는 함수
def check_list(lst):
    # 리스트의 0번째부터 체크
    check = [lst[0]]

    # 체크를 순회
    for c in check:
        # c번째 행의 요소들 순회
        for n in range(N):
            # 아직 체크에 없고 리스트에 있으면서 c와 연결되어 있으면
            if n not in check and n in lst and Rrc[c][n] == 1:
                # c에 추가
                check.append(n)

    # 모든 요소가 연결되어 있는지 판단 후 return
    if set(check) == set(lst):
        return True
    else:
        return False

for test_case in range(1,T+1):
    # 마을의 수
    N = int(input())
    # 마을 간 연결
    Rrc = [list(map(int,input().split())) for _ in range(N)]
    # 마을당 사람의 수
    people = list(map(int,input().split()))
    
    # 마을 인덱스
    arr = [num for num in range(N)]
    # 최솟값 변수
    min_result = float('inf')

    # 부분집합 구하기(0~2**n-1까지)
    # 단, 둘로 나누어지는 경우 중에서 중복을 제거한 경우만
    # 각 부분집합을 왼쪽 지역구라고 한다
    # 이때 선택되지 않은 원소들을 오른쪽 지역구라고 한다
    # 제거하려는 중복은 왼쪽 지역구의 경우와 오른쪽 지역구가 중복되는 경우
    # 예: [0,1,2]에서 0/1,2와 1,2/0는 중복인 경우
    # 부분집합들을 반으로 가르면 문제는 해결된다
    # 그리고 한쪽에 아무것도 없는 경우를 제거하면 된다

    # N개의 요소를 가진 부분집합을 중복없이 둘로 나눌 수 있는 경우만 생성
    for i in range(1,(1<<N)//2):
        # 왼쪽 지역구
        left = []
        for j in range(N):
            if i & (1<<j):
                left.append(arr[j])

        # 오른쪽 지역구(왼쪽에 없는 나머지)
        right = []
        for a in arr:
            if a not in left:
                right.append(a)

        # 왼쪽 지역구 연결 확인
        if len(left) > 1 and not check_list(left):
            continue
        # 오른쪽 지역구 연결 확인
        if len(right) > 1 and not check_list(right):
            continue
        
        # 지역구 간의 차
        result = abs(sum([people[l] for l in left]) - sum([people[r] for r in right]))
        # 최솟값 갱신
        if min_result > result:
            min_result = result

    print(f'#{test_case} {min_result}')
