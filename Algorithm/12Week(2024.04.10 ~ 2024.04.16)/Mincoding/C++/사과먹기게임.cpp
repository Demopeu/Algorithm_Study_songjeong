#include <iostream>
#include <vector>
#include <utility>

using namespace std;

pair<int, int> find_next(pair<int, int> start, pair<int, int> end, int now)
{
	int count = 0;
	int x = end.first - start.first;
	int y = end.second - start.second;

	while (true)
	{
		if (x == 0 && y == 0)
		{
			return make_pair(count, now);

		}
		if (now == 0) {
			if (y > 0) {
				y = 0;
			}
			else {
				now = 1;
				count += 1;
			}
		}
		else if (now == 1) {
			if (x > 0) {
				x = 0;
			}
			else {
				now = 2;
				count += 1;
			}
		}
		else if (now == 2) {
			if (y < 0) {
				y = 0;
			}
			else {
				now = 3;
				count += 1;
			}
		}
		else {
			if (x < 0) {
				x = 0;
			}
			else {
				now = 0;
				count += 1;
			}
		}

	}
}


int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0); cout.tie(0);
	int T;
	cin >> T;
	for (int test_case = 1; test_case < T + 1; test_case++)
	{
		int N, M = 0, now = 0, sum_count = 0;
		cin >> N;
		vector<vector<int>> matrix(N, vector<int>(N));
		vector<pair<int, int>> answer(10,make_pair(0, 0));
		for (int i = 0; i < N; i++)
		{
			for (int j = 0; j < N; j++)
			{
				int number;
				cin >> number;
				matrix[i][j] = number;
				if (number != 0)
				{	

					answer[number] = make_pair(i, j);
					M++;
				}
			}
		}
		for (int i = 0; i < M; i++)
		{
			pair<int, int>next_move = find_next(answer[i], answer[i + 1], now);
			sum_count += next_move.first;
			now = next_move.second;
		}
		cout << "#" << test_case << " " << sum_count << '\n';
	}
}


// 사과 먹기 게임
// 부실 코드임 ㅅㄱ