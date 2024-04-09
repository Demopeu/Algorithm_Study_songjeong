#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <tuple>
#include <climits>

using namespace std;

int dijstra(pair<int, int> start, pair<int, int> end, int N,int M,vector<vector<int>>& matrix) {
	int dx[4] = { 0,0,-1,1 }, dy[4] = { -1,1,0,0 };
	vector<vector<int>> max_list(N, vector<int>(M, INT_MAX));
	int s1, s2;
	s1 = start.first; s2 = start.second;
	priority_queue<tuple<int, int, int>, vector<tuple<int, int, int>>, greater<tuple<int, int, int>>> q;
	q.push(make_tuple(0,s1,s2 ));

	while (!(q.empty()))
	{
		int cost, x, y;
		tie(cost, x, y) = q.top();
		q.pop();

		if (x == end.first && y == end.second) {
			return cost;
		}
		else
		{
			for (int k = 1; k < N; k++)
			{
				for (int l = 0; l < 4; l++)
				{
					int nx, ny;
					nx = x + dx[l] * k;
					ny = y + dy[l];

					if (0 <= nx && nx < N && 0 <= ny && ny < M) {
						if (matrix[nx][ny] != 0) {
							cost = max(cost, abs(dx[l] * k));
							if (cost < max_list[nx][ny]) {
								max_list[nx][ny] = cost;
								q.push(make_tuple(cost, nx, ny));
							}
						}

					}
					else {

					}
				}
			}
		}
		
	}
	return -1;
}

int main()
{	
	ios_base::sync_with_stdio(false);
	cin.tie(0); cout.tie(0);
	int N, M;
	pair<int, int> start;
	pair<int, int> end;

	cin >> N >> M;
	vector<vector<int>> matrix(N, vector<int>(M));
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < M; j++)
		{
			int number;
			cin >> number;
			matrix[i][j] = number;
			if (number == 2) {
				start.first = i;
				start.second = j;
				
			}
			if (number == 3) {
				end.first = i;
				end.second = j;

			}
		}
	}

	int answer;
	answer = dijstra(start, end, N, M, matrix);
	cout << answer << endl;
	return 0;
}
