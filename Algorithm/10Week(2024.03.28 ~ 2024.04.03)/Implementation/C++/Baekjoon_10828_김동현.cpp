#include <iostream>
#include <string>
// c++은 stack 모듈이 있다
// top,size,pop,push,empty,swap 자동 탑재
//swap은 두 스택의 내용을 바꾸고 싶을 때 사용
#include <stack>
using namespace std;

int main()
{
	ios_base::sync_with_stdio(false);
	cout.tie(0); cin.tie(0);

	stack<int> stacks;
	int N,answer;
	string mission;
	cin >> N;

	for (int i = 0; i < N; i++)
	{
		cin >> mission;
		if (mission == "push")
		{
			int num;
			cin >> num;
			stacks.push(num);
		}
		else if (mission == "top")
		{
			if (stacks.size() == 0) {
				answer = -1;
				cout << answer << '\n';
			}
			else {
				answer = stacks.top();
				cout << answer << '\n';
			}
		}
		else if (mission == "empty")
		{
			if (stacks.size() == 0) {
				answer = 1;
				cout << answer << '\n';
			}
			else {
				answer = 0;
				cout << answer << '\n';
			}

		}
		else if (mission == "pop")
		{
			if (stacks.size() == 0) {
				answer = -1;
				cout << answer << '\n';
			}
			else {
				answer = stacks.top();
				cout << answer << '\n';
				stacks.pop();
			}

		}
		else {
			cout << stacks.size() << '\n';
		}
	}

	return 0;
}

//https://www.acmicpc.net/problem/10828
