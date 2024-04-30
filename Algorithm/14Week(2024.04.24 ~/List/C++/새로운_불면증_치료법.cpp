#include <iostream>
#include <string>
using namespace std;

int main()
{
	int T, N, checkNum = (1 << 10) - 1;
	cin >> T;
	for (int testcase = 1; testcase < T+1; testcase++)
	{		
		cin >> N;
		int visited = 0, count = 0;
		while (visited != checkNum)
		{
			int nowNum = N * (++count);
			string strNum = to_string(nowNum);
			for (char(c) : strNum )
			{
				int num = c - '0';
				visited |= (1 << num);
			}
		}
		
	cout << "#" << testcase << " " << N * count << endl;
	}
	return 0;
}