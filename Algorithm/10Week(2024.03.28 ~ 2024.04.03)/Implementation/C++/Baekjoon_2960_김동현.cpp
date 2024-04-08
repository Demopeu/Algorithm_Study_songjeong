#include <iostream>
using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int N, M, answer = 0;
	cin >> N >> M;
	bool arr[1001] = { false, false };

	for (int i = 2; i <= N; i++) {
		arr[i] = true;
	}

	for (int i = 2; i <= N; i++) {
		if (arr[i]) {
			for (int j = i; j <= N; j += i) {
				if (arr[j]) {
					arr[j] = false;
					answer += 1;
					if (answer == M) {
						cout << j << '\n';
					}
				}
			}
		}
	}
	return 0;
}
//https://www.acmicpc.net/problem/2960