#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0); cout.tie(0);
	int lcs[1001][1001];

	string a, b;
	cin >> a >> b;
	for (int i = 1; i < a.length()+1; i++)
	{
		for (int j = 1; j < b.length()+1; j++)
		{
			if (a[i-1]==b[j-1])
			{
				lcs[i][j] = lcs[i - 1][j - 1] + 1;
			}
			else
			{
				lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1]);
			}
		}
	}
	cout << lcs[a.length()][b.length()] << '\n';
	return 0;
}

//https://www.acmicpc.net/problem/9251
