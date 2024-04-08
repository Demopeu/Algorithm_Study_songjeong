import copy
from collections import deque

T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    work_time_lst = {}
    work_before_lst = []
    max_time_in_all = float('inf')

    for i in range(1, N+1):
        work_time, before_work_number, *before_work = map(int,input().split())
        work_time_lst[i] = work_time
        work_before_lst.append([i,before_work])
    work_before_lst.sort(key=lambda x: len(x[1]))

    for i in range(1, N+1):  # 코코 투입

        work_time_lst_in_coco = copy.deepcopy(work_time_lst)
        work_time_lst_in_coco[i] = work_time_lst_in_coco[i]//2
        work_before_lst_in_coco = deque(copy.deepcopy(work_before_lst))
        finished_work = []

        infinity_check = 0
        infinity_check_flag = False

        while work_before_lst_in_coco:

            Not_before_finish = False
            work, before_list = work_before_lst_in_coco.popleft()

            for j in before_list:
                if j not in finished_work:
                    Not_before_finish = True
                    break

            if Not_before_finish:
                work_before_lst_in_coco.append([work, before_list])
                infinity_check += 1
                if infinity_check == len(work_before_lst_in_coco):
                    infinity_check_flag = True
                    break
                continue
            else:
                infinity_check = 0

            finished_work.append(work)

            if len(before_list)>0:
                find_max_before_work_time = []
                for k in before_list:
                    find_max_before_work_time.append(work_time_lst_in_coco[k])
                work_time_lst_in_coco[work] += max(find_max_before_work_time)

        if infinity_check_flag:
            max_time_in_all = -1
            break

        max_time_in_all = min(max_time_in_all,max(work_time_lst_in_coco.values()))

    print(f'#{test_case} {max_time_in_all}')
