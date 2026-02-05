#include <iostream>
#include <vector>
using namespace std;


int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int N, M, temp;
	cin >> N >> M;

	vector<vector<int>> matrix(N, vector<int>(M));
	for (int i=0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			cin >> matrix[i][j];
		}
	}
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			cin >> temp;
			cout << matrix[i][j] + temp << ' ';
		}
		cout << '\n';
	}

	return 0;
}