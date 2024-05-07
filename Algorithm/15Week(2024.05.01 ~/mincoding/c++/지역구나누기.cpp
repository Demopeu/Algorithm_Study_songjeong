#include <iostream>
#include <vector>
#include <algorithm>
#include <deque>

using namespace std;
int T,N;

int bfs(vector<vector<int>> &graph,vector<int> &left, vector<int> &right) {
	deque<int> q;
	vector<bool> visited(N, false);
	q.push_back(left.front());
	visited[left.front()] = true;

	while (!(q.empty())){
		int node = q.front();
		q.pop_front();
		for (int v :graph[node]){
			if (!(visited[v]) && find(left.begin(), left.end(), v) != left.end()){
				visited[v] = true;
				q.push_back(v);
			}
		}
	}

	q.push_back(right.front());
	visited[right.front()] = true;

	while (!(q.empty())) {
		int node = q.front();
		q.pop_front();
		for (int v : graph[node]) {
			if (!(visited[v]) && find(right.begin(), right.end(), v) != right.end()) {
				visited[v] = true;
				q.push_back(v);
			}
		}
	}
	for (int i = 0; i < N; ++i) {
		if (!visited[i]) {
			return false;
		}
	}
	return true;
}
int main()
{
	cin >> T;
	for (int testcase = 1; testcase < T+1; testcase++){
		cout << '#' << testcase << " ";
		cin >> N;
		vector<vector<int>> graph(N);
		int number[9],sum_number=0;

		for (int i = 0; i < N; i++){
			for (int j = 0; j < N; j++){
				int num;
				cin >> num;
				if (num !=0){
					graph[i].push_back(j);
					graph[j].push_back(i);
				}
			}
		}
		for (int i = 0; i < N; i++){
			cin >> number[i];
			sum_number += number[i];
		}


		for (int i = 0; i < (1<<N); i++){
			vector<int> left,right;
			for (int j = 0; j < N; j++){
				if (i&(1 << j)) {
					left.push_back(j);
				}else{
					right.push_back(j);
				}
			}
			if (!(left.empty() || right.empty())) {
				if (bfs(graph, left, right)) {
					int left_sum = 0, right_sum = 0;
					for (int a : left) left_sum += number[a];
					for (int b : right) right_sum += number[b];
					sum_number = min(sum_number, abs(left_sum - right_sum));
				}
			}
		}

		cout << sum_number << '\n';
	}
	return 0;
}