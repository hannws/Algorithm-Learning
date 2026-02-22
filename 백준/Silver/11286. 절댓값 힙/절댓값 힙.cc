#include <iostream>
#include <queue>
using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	
	int N;
	cin >> N;

	auto cmp = [](int a, int b) {
		if (abs(a) == abs(b))
			return a > b;
		return abs(a) > abs(b);
		};

	priority_queue<int, vector<int>, decltype(cmp)> pq(cmp);
	for (int i = 0; i < N; i++) {
		int num;
		cin >> num;

		if (num == 0) {
			if (!pq.empty()) {
				cout << pq.top() << '\n';
				pq.pop();
			}
			else
				cout << 0 << '\n';
		}
		else {
			pq.push(num);
		}
	}
	return 0;
}