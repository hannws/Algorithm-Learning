#include <iostream>
#include <vector>
#include <string>
using namespace std;

void change(vector<vector<int>>& A, int r, int c) {
	for (int i = r; i < r + 3; i++) {
		for (int j = c; j < c + 3; j++) {
			A[i][j] = 1 - A[i][j];
		}
	}
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int n, m;
	cin >> n >> m;

	vector<vector<int>> A(n, vector<int>(m)), B(n, vector<int>(m));
	for (auto& i : A) {
		string row;
		cin >> row;
		for (int j = 0; j < m; j++)
			i[j] = row[j] - '0';
	}

	for (auto& i : B) {
		string row;
		cin >> row;
		for (int j = 0; j < m; j++)
			i[j] = row[j] - '0';
	}

	int cnt = 0;
	for (int i = 0; i <= n-3; i++) {
		for (int j = 0; j <= m-3; j++) {
			if (A[i][j] != B[i][j]) {
				change(A, i, j);
				cnt++;
			}
		}
	}

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++)
			if (A[i][j] != B[i][j]) {
				cout << -1;
				return 0;
			}
	}

	cout << cnt;
	return 0;
}