#include <iostream>
using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int N;
	cin >> N;

	if (N == 1) {
		cout << 1 << endl;
	}
	else {
		int i = 1;
		while (true) {
			int left = 3 * (i - 1) * i + 1;
			int right = 3 * i * (i + 1) + 1;

			if (left < N && N <= right) {
				cout << i + 1;
				break;
			}
			i++;
		}
	}
	return 0;
}