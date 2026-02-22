#include <iostream>
#include <queue>
using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	int N;
	cin >> N;

	int dasom;
	cin >> dasom;

	if (N == 1) {
		cout << 0;
		return 0;
	}

	priority_queue<int> pq;

	for (int i = 0; i < N - 1; i++) {
		int vote;
		cin >> vote;
		pq.push(vote);
	}

	int buy = 0;

	while (!pq.empty() && pq.top() >= dasom) {
		int top = pq.top();
		pq.pop();

		top--;
		dasom++;
		buy++;

		pq.push(top);
	}

	cout << buy;

	return 0;
}