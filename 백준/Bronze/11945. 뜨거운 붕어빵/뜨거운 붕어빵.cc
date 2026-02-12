#include <iostream>
#include <string>
using namespace std;


int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	int N, M;
	cin >> N >> M;

	string S;
	for (int i = 0; i < N; i++) {
		cin >> S;

		for (int j = 1; j <= M; j++) {
			cout << S[M - j];
		}
		cout << '\n';
	}
	return 0;
}