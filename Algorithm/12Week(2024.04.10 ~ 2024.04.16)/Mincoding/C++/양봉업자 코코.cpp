#include <iostream>
#include <vector>
#include <algorithm>
#include <deque>
#include <tuple>
#include<functional>

using namespace std;

int BFS(int x, int y, int N, int M, vector<vector<int>> & matrix) {
	int find=0,hunny = 0;
	deque<tuple<int, int, int, int>> q;
	q.push_back(make_tuple(x, y, matrix[x][y], 1));
	vector<vector<bool>> visited(N, vector<bool>(M, false));
	vector<int> hunny_arr(6);

	int dx_odd[6] = { 0,0,-1,1,1,1 };
	int dy_odd[6] = { -1,1,0,0,-1,1 };
	int dx_evl[6] = { 0,0,-1,1,-1,-1 };
	int dy_evl[6] = { -1,1,0,0,-1,1 };

	int *dx_, *dy_;
	if (y % 2 != 0)
	{
		dx_ = dx_odd;
		dy_ = dy_odd;
	}
	else {
		dx_ = dx_evl;
		dy_ = dy_evl;
	}
	for (int l = 0; l < 6; l++) {
		int nx = x + dx_[l];
		int ny = y + dy_[l];
		if (0 <= nx && nx < N && 0 <= ny && ny < M) {
			hunny_arr[find] = matrix[nx][ny];
			find += 1;
		}
	}
	if (hunny_arr.size() > 2)
	{
		sort(hunny_arr.begin(), hunny_arr.end(), greater<int>());
		for (int i = 0; i < 3; i++)
		{
			hunny += hunny_arr[i];
		}
	}
	hunny += matrix[x][y];
	while (!(q.empty()))
	{
		int x, y, sum_number, count;
		tie(x, y, sum_number, count) = q.front();
		q.pop_front();
		visited[x][y] = true;

		int *dx, *dy;
		if (y % 2 != 0)
		{
			dx = dx_odd;
			dy = dy_odd;
		}
		else {
			dx = dx_evl;
			dy = dy_evl;
		}
		for (int l = 0; l < 6; l++) {
			int nx = x + dx[l];
			int ny = y + dy[l];
			if (0 <= nx && nx < N && 0 <= ny && ny < M && !visited[nx][ny]) {
				int new_sum_number = sum_number + matrix[nx][ny];
				if (count == 3) {
					hunny = max(hunny, new_sum_number);
					continue;
				}
				q.push_back(make_tuple(nx, ny, new_sum_number, count + 1));
			}
		}
	}
		return hunny;
	}

int main()
{
	int T;
	cin >> T;
	for (int test_case = 1; test_case <T+1 ; test_case++)
	{
		int N, M, max_hunny_count = 0;
		cin >> N >> M;
		vector<vector<int>> matrix(N,vector<int>(M));
		for (int i = 0; i < N; i++)
		{
			for (int j = 0; j < M; j++)
			{
				cin >> matrix[i][j];;
			}
		}
		for (int i = 0; i < N; i++)
		{
			for (int j = 0; j < M; j++)
			{
				max_hunny_count = max(max_hunny_count, BFS(i, j,N,M,matrix));
			}
		}
		cout << "#" << test_case << " " << max_hunny_count << "\n";
	}
	return 0;
}
