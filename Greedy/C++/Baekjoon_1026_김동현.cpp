#include <iostream>
#include<algorithm>

using namespace std;
int main(){	
	ios_base::sync_with_stdio(false);
	cin.tie(0); cout.tie(0);
	int N,A[50],B[50],answer=0;
	cin >> N;
	for (int i = 0; i < N; i++) {
		cin >> A[i];
		//cout << A[i] << '\n';
	}
	for (int i = 0; i < N; i++) {
		cin >> B[i];
		//cout << B[i] << '\n';
	}
	sort(A,A+N);
	sort(B, B + N,greater<int>());

	for (int i = 0; i < N; i++)
	{
		answer += A[i] * B[i];
	}
	cout << answer << '\n';
	return 0;
}

//https://www.acmicpc.net/problem/1026
//놀라운 사실 c++는 1개씩 쪼개서 받아야함 개열받네