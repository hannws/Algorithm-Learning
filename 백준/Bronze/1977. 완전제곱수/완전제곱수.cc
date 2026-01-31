#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int M, N;
	cin >> M >> N;

	int start = ceil(sqrt(M));
	int end = floor(sqrt(N));

	int sum = 0;
	for (int i = start; i <= end; i++) {
		sum += i * i;
	}

	if (sum == 0) {
		cout << -1 << endl;
	}
	else {
		cout << sum << '\n';
		cout << start * start << endl;
	}
	return 0;
}