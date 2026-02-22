#include <iostream>
#include <queue>
using namespace std;

struct cmp {
	bool operator()(int a, int b){
		if (abs(a) == abs(b))
			return a > b;
		return abs(a) > abs(b);
	}
};

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	
	int N;
	cin >> N;

	priority_queue<int, vector<int>, cmp> pq;
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