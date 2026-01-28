#include <iostream>
using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int N;
	cin >> N;

	int count = 1, range=1;
	while (N > range) {
		range += 6 * count;
		count++;
	}

	cout << count;
	return 0;
}