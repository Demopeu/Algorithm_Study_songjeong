#include <iostream>
// 문자열을 받기 위해서
#include<string>

using namespace std;
int main(){	
	ios_base::sync_with_stdio(false);
	cout.tie(0); cin.tie(0);
	
	string input,num;
	cin >> input;

	int answer = 0;
	bool TF = false;
	for (int i = 0; i <= input.size(); i++)
	{
		if (input[i] == '-' || input[i] == '+'||i==input.size())
		{
			if (TF)
			{
				// 문자열을 숫자로 -> std::stoi
				answer -= stoi(num);
				num = "";
			}
			else
			{
				answer += stoi(num);
				num = "";
			}
		}
		else
		{
			num += input[i];
		}
		if (input[i] == '-')
		{
			TF = true;
		}
	}
	cout << answer<<'\n';
	return 0;
}

// https://www.acmicpc.net/problem/1541
