#include <iostream>
using namespace std;

int main(){	
	ios_base::sync_with_stdio(false);
	cin.tie(0); cout.tie(0);

	int en[6] = { 500,100,50,10,5,1 };

	int money,otsuri,count;
	cin >> money;
	otsuri = 1000-money;
	count = 0;
	for (int i = 0; i < 6; i++) {
		count += (otsuri / en[i]);
		//cout << count << '\n';
		otsuri %= en[i];
	}

	cout <<count << '\n';
	return 0;
}

// https://www.acmicpc.net/problem/5585
