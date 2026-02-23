#include <iostream>
#include <vector>
using namespace std;

long long mod = 1000000007;
vector<long long> nums;
vector<long long> segtree;

//트리 제작
long long build(int node, int start, int end) {
	if (start == end) 
		return segtree[node] = nums[start];
	

	int mid = (start + end) / 2;

	long long left = build(2 * node, start, mid);
	long long right = build(2 * node + 1, mid + 1, end);

	return segtree[node] = (left*right)%mod;
}

void update(int node, int start, int end, int idx, long long value) {
	if (idx < start || idx > end)
		return;

	if (start == end) {
		nums[idx] = value%mod;
		segtree[node] = nums[idx];
		return;
	}

	int mid = (start + end) / 2;
	
	update(node * 2, start, mid, idx, value);
	update(node * 2 + 1, mid + 1, end, idx, value);

	segtree[node] = (segtree[node * 2] * segtree[node * 2 + 1]) % mod;
}

long long query(int node, int start, int end, int left, int right) {
	if (right < start || left > end)
		return 1;

	if (left <= start && end <= right)
		return segtree[node];

	int mid = (start + end) / 2;

	long long l = query(node * 2, start, mid, left, right);
	long long r = query(node * 2 + 1, mid + 1, end, left, right);

	return (l * r) % mod;
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	
	long long N, M, K;
	cin >> N >> M >> K;

	nums.resize(N);
	segtree.resize(4 * N);
	
	for (auto& i : nums)
		cin >> i;

	build(1, 0, N - 1);

	for (int i = 0; i < M + K; i++) {
		int a, b, c;
		cin >> a >> b >> c;

		if (a == 1) {
			update(1, 0, N - 1, b - 1, c);
		}
		else if (a == 2) {
			cout << query(1, 0, N - 1, b - 1, c - 1) << '\n';
		}
	}
	return 0;
}