#include <iostream>
#include <deque>
using namespace std;


int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	
	deque<int> dq;
	int N;
	cin >> N;

	for (int i = 1; i <= N; i++)
		dq.push_back(i);

	while (true) {
		cout << dq.front();
		
		dq.pop_front();
		if (!dq.empty())
			cout << ' ';
		else
			break;

		dq.push_back(dq.front());
		dq.pop_front();
	}

	return 0;
}