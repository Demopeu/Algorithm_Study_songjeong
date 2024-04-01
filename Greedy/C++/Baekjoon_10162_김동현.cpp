#include <iostream>
using namespace std;

int main(){	
	// c와 c++ 동기화를 비활성화
	// c스타일 코드를 못쓰지만 그만큼 버퍼를 안쓰기 때문에 시간 속도 빨라짐
	ios_base::sync_with_stdio(false);
	// 원래 cin과 cout는 하나로 묶어지는데 이부분이 시간이 많이 걸림
	// 이것을 수행하지 않으므로, 시간 속도가 빨라지고, cin 출력 전에 cout 가능
	cin.tie(0); cout.tie(0);

	int T;
	cin >> T;

	if (T % 10 != 0) {
		cout << -1 << '\n';
		return 0;
	}

	int a = T / 300;
	T %= 300;

	int b = T / 60;
	T %= 60;
	
	int c = T / 10;

	cout << a << ' ' << b << ' ' << c << '\n';

	return 0;
    
}

//https://www.acmicpc.net/problem/10162