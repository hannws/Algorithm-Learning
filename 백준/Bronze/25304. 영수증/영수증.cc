#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	
	int price, N, a, b, realprice=0;
	cin >> price >> N;
	
	for (int i = 0; i < N; i++) {
		cin >> a >> b;
		realprice += a * b;
	}
	if (realprice == price) {
		cout << "Yes" << '\n';
	}
	else {
		cout << "No" << '\n';
	}
	return 0;
}