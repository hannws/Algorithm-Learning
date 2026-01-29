#include <iostream>
#include <vector>
using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int N, M;
	cin >> N >> M;

	vector<int> total(N+1, 0);
	for (int i = 0; i < N; i++) {
		int temp;
		cin >> temp;
		total[i + 1] += total[i] + temp;
	}

	int start, end;
	while (M--) {
		cin >> start >> end;
		cout << total[end] - total[start-1] << '\n';
	}

	return 0;
}