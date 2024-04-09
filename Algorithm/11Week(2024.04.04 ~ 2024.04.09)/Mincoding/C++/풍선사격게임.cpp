#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

int dfs(vector<int>& array) {
	int max_number = 0;
	queue<pair<int, vector<int>>> q;
	q.push(make_pair(0, array));
	while (!(q.empty())) {
		int sum_number = q.front().first;
		array = q.front().second;
		q.pop();
		if (array.size() == 3) {
			max_number = max(max_number, sum_number + array[1]);
			continue;
		}
		for (size_t i = 1; i < array.size() - 1; i++) {
			vector<int> new_array(array.begin(), array.end());
			new_array.erase(new_array.begin() + i);
			q.push(make_pair(sum_number + array[i - 1] * array[i + 1], new_array));
		}

	}
	return max_number;
}

int main()
{	
	ios_base::sync_with_stdio(false);
	cin.tie(0); cout.tie(0);
	int T;
	cin >> T;
	for (size_t test_case = 1; test_case < T+1; test_case++)
	{
		int N;
		cin >> N;
		vector<int>array;
		array.push_back(1);
		for (size_t i = 0; i < N; i++)
		{
			int num;
			cin >> num;
			array.push_back(num);
		}
		array.push_back(1);
		cout << "#" << test_case << " " << dfs(array) << endl;
	}
	return 0;
}

// 파이썬 시간초과 코드 개빡쳐서 걍 C++로 풀엇음
// def dfs(lst):
//     max_number = 0
//     queue = [(0,lst)]
//     while queue:
//         sum_number,lst = queue.pop()
//         if len(lst) == 3:
//             max_number = max(max_number,sum_number+lst[1])
//             continue
//         for i in range(1,len(lst)-1):
//             new_lst = lst[:i]+lst[i+1:]
//             queue.append((sum_number+lst[i-1]*lst[i+1],new_lst))
//     return max_number


// T = int(input())
// for test_case in range(1,T+1):
//     N = int(input())
//     lst = [1]+list(map(int,input().split()))+[1]
//     print(f'#{test_case} {dfs(lst)}')