#include <iostream>
using namespace std;

int main(){	
	cin.tie(0); cout.tie(0);
	ios_base::sync_with_stdio(false);
	cin.tie(0); cout.tie(0);

	int N, K, answer,arr[11];
	cin >> N >> K;

	for (int i = 0; i < N; i++)
	{
		cin >> arr[i];
	}
	answer = 0;
	for (int i = N-1; i > -1; i--)
	{
		answer += K / arr[i];
		K %= arr[i];
	}
	cout << answer << '\n';
	return 0;
}
//https://www.acmicpc.net/problem/11047