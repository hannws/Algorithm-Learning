#include <iostream>
#include <vector>
using namespace std;


int main() {
	int A, B, C;
	cin >> A >> B >> C;

	vector<pair<int, int>> truck(3);
	for (int i = 0; i < 3; i++) {
		cin >> truck[i].first >> truck[i].second;
	}

	vector<int> cnt(101, 0);

	for (int i = 0; i < 3; i++) {
		int s = truck[i].first;
		int e = truck[i].second;
		for (int t = s; t < e; t++) {
			cnt[t]++;
		}
	}

	int result = 0;

	for (int t = 1; t <= 100; t++) {
		if (cnt[t] == 1) result += A;
		else if (cnt[t] == 2) result += B * 2;
		else if (cnt[t] == 3) result += 3 * C;
	}

	cout << result << endl;
	return 0;
}