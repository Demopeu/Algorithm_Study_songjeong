#include <iostream>
// sort 쓰려고
#include<algorithm>
// pair 쓰려고
#include<utility>

using namespace std;
int main(){	
	ios_base::sync_with_stdio(false);
	cin.tie(0); cout.tie(0);

	// pair 배열
	// pair<변수타입,변수타입> 변수이름[변수크기];
	pair<int, int> arr[100001];
	int N,start,end,now,count = 1;
	cin >> N;
	for (int i = 0; i < N+1; i++)
	{
		cin >> start >> end;
		arr[i] = { end,start };
	}
	// sort - arr의 처음부터 arr의 N번까지 요소를 정렬하겠다 first 기준
	sort(arr,arr+N);
	now = arr[0].first;
	for (int i = 1; i < N; i++)
	{
		if (now<=arr[i].second)
		{
			count += 1;
			now = arr[i].first;
		}
	}
	cout << count;
	return 0;
}

//https://www.acmicpc.net/problem/1931