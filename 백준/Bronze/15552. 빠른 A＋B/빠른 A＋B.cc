#include <iostream>
using namespace std;


int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int test, A, B;
	cin >> test;
	while (test--) {
		cin >> A >> B;
		cout << A + B << '\n';
	}
	return 0;
}