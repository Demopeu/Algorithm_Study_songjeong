#include <iostream>

using namespace std;

int main()
{	
	ios_base::sync_with_stdio(false);
	cin.tie(0); cout.tie(0);
	int N,M,B,floor=0,num=100000000000;
	cin >> N >> M >> B;
	int matrix[500][500];
	for (int i = 0; i < N; i++)
	{
		for (int j = 0; j < M; j++)
		{
			int answer;
			cin >> answer;
			matrix[i][j] = answer;
		}
	}
	for (int h = 0; h < 257; h++)
	{
		int plus = 0, minus = 0;
		for (int i = 0; i < N; i++)
		{
			for (int j = 0; j < M; j++)
			{
				//int result;
				//result = matrix[i][j];
				if (matrix[i][j]>h)
				{
					plus += matrix[i][j] - h;
				}
				if (h > matrix[i][j])
				{
					minus += h - matrix[i][j];
				}
			}

		}
		if (plus + B >= minus) {
			if (plus * 2 + minus <= num) {
				num = plus * 2 + minus;
				floor = h;
			}
		}
	}
	cout << num <<" "<< floor << '\n';
	return 0;
}

//https://www.acmicpc.net/problem/18111
