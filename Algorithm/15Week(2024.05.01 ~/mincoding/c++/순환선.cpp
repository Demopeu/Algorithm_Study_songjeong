#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;
int T,N;
int main()
{
	cin >> T;
	for (int testcase = 1; testcase < T + 1; testcase++) {
		cout << '#' << testcase << " ";
		cin >> N;
		vector<int> lst(N);
		for (int i = 0; i < N; i++) {
			cin >> lst[i];
		}
		int answer = 0;
		for (int a = 0; a < N; a++) {
			for (int b = a + 1; b < N; b++) {
				for (int c = b + 1; c < N; c++) {
					for (int d = c + 1; d < N; d++) {
						if (d - c <= 1 || c - b <= 1 || b - a <= 1 || a + N - d <= 1) {
							continue;
						}
						int SUM_a = pow(lst[d] + lst[a], 2) + pow(lst[c] + lst[b], 2);
						int SUM_b = pow(lst[b] + lst[a], 2) + pow(lst[d] + lst[c], 2);
						answer = max(answer, max(SUM_a, SUM_b));
					}
				}
			}
		}
		cout << answer << '\n';

	}
	return 0;
}