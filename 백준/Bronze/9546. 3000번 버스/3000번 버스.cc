#include <iostream>
using namespace std;


int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	int N;
	cin >> N;
	while (N--) {
		int k, result;
		cin >> k;
		result = 1;
		while (--k) {
			result = (result + 0.5) * 2;
		}
		cout << result << '\n';
	}
	return 0;
}