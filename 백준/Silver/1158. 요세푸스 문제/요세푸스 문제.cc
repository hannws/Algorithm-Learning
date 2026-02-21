#include <iostream>
#include <vector>
using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int N, K;
	cin >> N >> K;

	vector<int> circle(N), result = {};
	for (int i = 0; i < N; i++)
		circle[i] = i + 1;

	int curr = 0;
	K = K - 1;
	for (int i = 0; i < N; i++) {
		curr = (curr + K) % circle.size();
		result.push_back(circle[curr]);
		circle.erase(circle.begin() + curr);
	}

	cout << '<';
	for (int i = 0; i < N - 1; i++) {
		cout << result[i] << ", ";
	}
	cout << result[N - 1] << '>';
	return 0;
}