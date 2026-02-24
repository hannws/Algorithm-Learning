#include <iostream>
#include <vector>
using namespace std;

const int INF = 1000000000;
vector<int> nums;
vector<int> tree;

int build(int node, int start, int end) {
	if (start == end)
		return tree[node] = nums[start];

	int mid = (start + end) / 2;
	int left = build(2 * node, start, mid);
	int right = build(2 * node + 1, mid + 1, end);

	return tree[node] = min(left, right);
}

int query(int node, int start, int end, int a, int b) {
	if (a > end || b < start)
		return INF;

	if (start >= a && b >= end)
		return tree[node];

	int mid = (start + end) / 2;
	int left = query(2 * node, start, mid, a, b);
	int right = query(2 * node+1, mid + 1, end, a, b);

	return min(left, right);
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	
	int N, M;
	cin >> N >> M;

	nums.resize(N);
	tree.resize(4 * N);

	for (int& i : nums)
		cin >> i;

	build(1, 0, N - 1);

	for (int i = 0; i < M; i++) {
		int a, b;
		cin >> a >> b;
		int p = query(1, 0, N - 1, a-1, b-1);
		
		cout << p << '\n';
	}
	return 0;
}