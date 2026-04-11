#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;


int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int N;
	cin >> N;

	if (N > 1e4) {
		cout << "Time limit exceeded" << '\n';
	}
	else
		cout << "Accepted" << '\n';

	return 0;
}