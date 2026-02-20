#include <iostream>
using namespace std;


int main() {
	int a, t;
	cin >> a >> t;

	int ans = 10 + 2 * (25 - a + t);
	cout << (ans <= 0 ? 0 : ans);
	return 0;
}