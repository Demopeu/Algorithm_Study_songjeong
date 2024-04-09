#include <iostream>
#include <string>

using namespace std;


int main()
{	
	ios_base::sync_with_stdio(false);
	cin.tie(0); cout.tie(0);
	int N, answer=0;
	cin >> N;
	for (int i = 1; i < N+1; i++)
	{
		string num = to_string(i);
		if (num.size() < 3) {
			answer += 1;
		}
		else
		{
			bool flag = true;
			for (int j = 0; j < num.size()-2; j++)
			{
				if (num[j] - '0' - (num[j + 1] - '0') != num[j + 1] - '0' - (num[j + 2] - '0')) {
					flag = false;
					break;
				}
				if (flag) {
					answer += 1;
			}
			}
		}
	}
	cout << answer << '\n';
	return 0;
}
// https://www.acmicpc.net/problem/1065