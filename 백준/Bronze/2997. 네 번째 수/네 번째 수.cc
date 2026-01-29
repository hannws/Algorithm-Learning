#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	vector<int> nums(3, 0);
	for (int i = 0; i < 3; i++) {
		cin >> nums[i];
	}
	sort(nums.begin(), nums.end());
	
	int interval;
	if (nums[1] - nums[0] < nums[2] - nums[1]) {
		interval = nums[1] - nums[0];
		cout << nums[1] + interval << endl;
	}
	else if (nums[1] - nums[0] == nums[2] - nums[1]) {
		interval = nums[1] - nums[0];
		cout << nums[2] + interval << endl;
	}
	else {
		interval = nums[2] - nums[1];
		cout << nums[0] + interval << endl;
	}

	return 0;
}