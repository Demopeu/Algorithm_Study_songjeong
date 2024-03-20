import sys
input = sys.stdin.readline

from collections import deque

def bfs():
    q = deque()
    q.append((start[0], start[1], 0))
    time_list = [[250001] * W for _ in range(H)]
    time_list[start[0]][start[1]] = 0

    while q:
        row, col, time_ = q.popleft()

        if time_ > time_list[row][col]:
            continue

        time_list[row][col] = time_

        if (row, col) == end:
            print(time_)
            return

        for i in range(4):
            nrow, ncol = row + d[i][0], col + d[i][1]

            if not (0 <= nrow < H and 0 <= ncol < W) or list_[nrow][ncol] == 2:
                continue

            if list_[row][col] == 3 and list_[nrow][ncol] == 3:
                if time_ < time_list[nrow][ncol]:
                    time_list[nrow][ncol] = time_
                    q.appendleft((nrow, ncol, time_))
            else:
                if time_ + 1 < time_list[nrow][ncol]:
                    time_list[nrow][ncol] = time_ + 1
                    q.append((nrow, ncol, time_ + 1))

H, W = map(int, input().split())
list_ = [list(input()) for _ in range(H)]
d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
start = end = 0

for row in range(H):
    for col in range(W):
        if list_[row][col] == 'S':
            list_[row][col] = 1
            start = (row, col)
        elif list_[row][col] == 'E':
            list_[row][col] = 1
            end = (row, col)
        elif list_[row][col] == '#':
            list_[row][col] = 2
        else:
            list_[row][col] = 0

for row in range(H):
    for col in  range(W):
        if list_[row][col] == 2:
            for i in range(4):
                nrow, ncol = row + d[i][0], col + d[i][1]

                if 0 <= nrow < H and 0 <= ncol < W and list_[nrow][ncol] != 2:
                    list_[nrow][ncol] = 3

bfs()