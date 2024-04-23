#include <iostream>

using namespace std;
int arr[30];

int main()
{
	int N;
	cin >> N;
	arr[0] = 1; arr[1] = 1;
	for (int i = 1; i < N; i++)
	{
		arr[i + 1] = arr[i] * 2;
		if (i - 3 >= 0 && (i - 2) % 2 == 1) arr[i + 1] -= arr[i - 3];
		if (i - 4 >= 0 && (i - 3) % 2 == 0) arr[i + 1] -= arr[i - 4];
	}
	cout << arr[N];
	return 0;
}

// https://www.acmicpc.net/problem/17291
// 0ms의 위엄
