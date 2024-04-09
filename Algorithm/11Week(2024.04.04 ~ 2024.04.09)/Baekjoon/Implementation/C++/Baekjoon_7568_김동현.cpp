#include <iostream>
#include <utility>
#include <algorithm>

using namespace std;

int main()
{	
	ios_base::sync_with_stdio(false);
	cin.tie(0); cout.tie(0);
	int N;
	pair<int, int> array[51];
	cin >> N;
	for (int i = 0; i < N; i++)
	{	
		int a, b;
		cin >> a>>b;
		array[i] = make_pair(a, b);
	}
	
	//sort(begin(array),end(array),greater<pair<int, int>>());

	for (int i = 0; i < N; i++)
	{
		int one, two,number;
		number = 0;

		one = array[i].first;
		two = array[i].second;

		for (int j = 0; j < N; j++)
		{
			int three, four;
			three = array[j].first;
			four = array[j].second;

			if (one < three && two < four)
			{
				number += 1;
			}
		}
		cout << number+1<<'\n';
	}

	return 0;
}

//https://www.acmicpc.net/problem/7568
