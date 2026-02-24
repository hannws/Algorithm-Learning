#include <iostream>
#include <vector>
using namespace std;

const int INF = 1e9;
vector<int> nums;
vector<pair<int, int>> tree;

pair<int, int> build(int node, int start, int end) {
	if (start == end)
		return tree[node] = {nums[start], nums[start]};

	int mid = (start + end) / 2;
	pair<int, int> left = build(2 * node, start, mid);
	pair<int, int> right = build(2 * node + 1, mid + 1, end);

	return tree[node] = { min(left.first, right.first), max(left.second, right.second) };
}

pair<int, int> query(int node, int start, int end, int a, int b) {
	if (a > end || b < start)
		return {INF, 0};

	if (start >= a && b >= end)
		return tree[node];

	int mid = (start + end) / 2;
	pair<int, int> left = query(2 * node, start, mid, a, b);
	pair<int, int> right = query(2 * node+1, mid + 1, end, a, b);

	return { min(left.first, right.first), max(left.second, right.second) };
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
		pair<int, int> p = query(1, 0, N - 1, a-1, b-1);
		
		cout << p.first << ' ' << p.second << '\n';
	}
	return 0;
}