#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int M, N;
	if (!(cin >> M >> N)) {
		return 0;
	}
	
	vector<int> nums;
	int start = int(sqrt(M)) - 1;
	int end = int(sqrt(N));
	int total = 0;

	for (int i = start; i <= end; i++) {
		if (i * i >= M && i * i <= N) {
			nums.push_back(i * i);
			total += i * i;
		}
	}
	if (nums.empty()) {
		cout << -1 << endl;
	}
	else {
		cout << total << '\n';
		cout << nums[0] << endl;
	}
	

	return 0;


}