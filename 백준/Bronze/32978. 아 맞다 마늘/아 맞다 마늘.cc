#include <iostream>
#include <unordered_map>
using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int N;
	cin >> N;

	unordered_map<string, int> m;

	for (int i = 0; i < N; i++) {
		string s;
		cin >> s;
		m[s]++;
	}

	for (int i = 0; i < N - 1; i++) {
		string s;
		cin >> s;
		m[s]--;
	}

	for (auto& p : m) {
		if (p.second == 1) {
			cout << p.first;
			break;
		}
	}
	return 0;
}