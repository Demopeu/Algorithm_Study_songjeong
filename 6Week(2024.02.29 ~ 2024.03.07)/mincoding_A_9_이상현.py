from itertools import combinations

T = int(input())

for tc in range(T):
    N = int(input())
    station_list = [n for n in range(N)]
    list_ = list(combinations(station_list, 2))
    cost_list = list(map(int, input().split()))
    max_ = 0

    for station in list_:
        if abs(station[1] - station[0]) == 1 or abs(station[1] - station[0]) == N - 1:
            continue

        temp1 = [n for n in range(station[0] + 2, station[1] - 1)]
        temp2 = [n for n in range(station[0] - 1)] + [n for n in range(station[1] + 2, N)]

        other_station_list = list(combinations(temp1, 2)) + list(combinations(temp2, 2))
        cost1 = (cost_list[station[0]] + cost_list[station[1]]) ** 2

        for other_station in other_station_list:
            if not other_station or abs(other_station[1] - other_station[0]) == 1 or abs(other_station[1] - other_station[0]) == N - 1:
                continue

            if abs(station[0] - other_station[1]) == N - 1 or abs(other_station[0] - station[1]) == N - 1:
                continue

            max_ = max(max_, (cost_list[other_station[0]] + cost_list[other_station[1]]) ** 2 + cost1)

    print(f'#{tc + 1} {max_}')