#include <iostream>
#include <vector>
#include <queue>
#include <climits>
#include <tuple>

using namespace std;

int dx[4] = { 0, 0, -1, 1 }, dy[4] = { -1, 1,0,0 };

int dijkstra(int N, int M,vector<vector<int>>&matrix, vector<vector<int>>&tunnel) {
	vector<vector<int>> min_lst(N, vector<int>(N, INT_MAX));
	min_lst[0][0] = 0;

	priority_queue <tuple<int, int, int, bool>, vector<tuple<int, int, int, bool>>, greater<tuple<int, int, int, bool>>> pq;
	pq.push( make_tuple(0,0,0,false));
	while (!(pq.empty())){
		int dist, x, y;bool used;
		tie(dist, x, y, used) = pq.top();
		pq.pop();

		if (x == N - 1 && y == N - 1) {
			return dist;
		}

		if (!(used)) {
			for (auto&t : tunnel) {
				if (x == t[0] && y == t[1] && dist + t[4] < min_lst[t[2]][t[3]]) {
					pq.push({ dist + t[4], t[2], t[3], true });
				}
				if (x == t[2] && y == t[3] && dist + t[4] < min_lst[t[0]][t[1]]) {
					pq.push({ dist + t[4], t[0], t[1], true });
				}
			}
		}
		for (int k = 0; k < 4; k++) {
			int nx = x + dx[k], ny = y + dy[k];
			if (nx >= 0 && nx < N && ny >= 0 && ny < N) {
				int cost = matrix[x][y] - matrix[nx][ny];
				if (cost > 0 && dist < min_lst[nx][ny]) {
					min_lst[nx][ny] = dist;
					pq.push({ dist, nx, ny, false });
				}
				else if (cost == 0 && dist + 1 < min_lst[nx][ny]) {
					min_lst[nx][ny] = dist + 1;
					pq.push({ dist + 1, nx, ny, false });
				}
				else if (cost < 0 && dist + (-cost) * 2 < min_lst[nx][ny]) {
					min_lst[nx][ny] = dist + (-cost) * 2;
					pq.push({ dist + (-cost) * 2, nx, ny, false });
				}
			}
		}
	}
	return -1;
}

using namespace std;
int T,N,M;
int main(){
	cin >> T;
	for (int testcase = 1; testcase < T + 1; testcase++) {
		cout << '#' << testcase << " ";
		cin >> N >> M;
		vector<vector<int>> matrix(N, vector<int>(N));
		vector<vector<int>> tunnel(M, vector<int>(5));
		for (int i = 0; i < N; i++){
			for (int j = 0; j < N; j++){
				int num;
				cin >> num;
				matrix[i][j] = num;
			}
		}
		for (int i = 0; i < M; i++){
			int x1, y1, x2, y2, fuel;
			cin >> x1 >> y1 >> x2 >> y2 >> fuel;
			tunnel[i][0] = x1-1;
			tunnel[i][1] = y1-1;
			tunnel[i][2] = x2-1;
			tunnel[i][3] = y2-1;
			tunnel[i][4] = fuel;
			}

		cout << dijkstra(N,M,matrix,tunnel) << '\n';
		}
	}