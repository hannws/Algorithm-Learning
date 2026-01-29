#include <iostream>
#include <vector>
using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int N, M;
	cin >> N >> M;

	vector<int> card(N);
	for (int i = 0; i < N; i++) {
		cin >> card[i];
	}

	int close = -1;
	for (int i = 0; i < N - 2; i++) {
		for (int j = i+1; j < N - 1; j++) {
			for (int k = j + 1; k < N; k++) {
				int num = card[i] + card[j] + card[k];
				if (num > close && num <= M) {
					close = num;
				}
				if (close == M) {
					cout << close << endl;
					return 0;
				}
			}
		}
	}

	cout << close << endl;
	return 0;
}