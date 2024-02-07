import sys

n = int(sys.stdin.readline().strip())
num_lst = []
# ZeroDivisionError 예외 처리 ver.1
try:
    for _ in range(n):
        num_lst.append(int(sys.stdin.readline().strip()))

    num_lst.sort() # sorted()는 메모리 사용량 2배, 속도 sort()가 더 빠름
    
    cut_cnt = float(n * 0.3 / 2)
    # 만약 정수 자리 부분이 짝수라면 1^(-9) 더해서 반올림 함수 round 사용
    if (cut_cnt - int(cut_cnt)) == 0.5 and int(cut_cnt) % 2 == 0:
        cut_cnt += 1e-9 # 1^(-9)

    cut_cnt = round(cut_cnt)    # 내장 함수 round는 소수점 자리가 0.5일때, 정수 자리 홀수면 올림, 짝수면 내림으로 구현되어있음 
    average = float(sum(num_lst[cut_cnt : n - cut_cnt]) / len(num_lst[cut_cnt : n - cut_cnt]))  # 아무 의견이 없을 때 ZeroDivisionError 발생

    if (average - int(average)) == 0.5 and int(average) % 2 == 0:
        average += 1e-9
    print(round(average))
except ZeroDivisionError:
    print(0)

# 런타임 에러(ZeroDivisionError) 예외 처리 ver.2
# if n == 0:
#     print(0)
#     exit()
# 시간 초과로 input() -> sys.stdin.readline()으로 변경
# 틀렸습니다 만나서 디버깅 중 짝수일 때 0.1을 더하는 부분이 문제가 될 것이라 생각해서 아주 작은 수인 1e-9 더하는 걸로 변경
# 혹시 몰라서 readline 뒤 공백, 개행문자 제거하는 .strip()도 추가


# 시간 복잡도: O(nlog(n))
# 출처: https://www.acmicpc.net/problem/18110