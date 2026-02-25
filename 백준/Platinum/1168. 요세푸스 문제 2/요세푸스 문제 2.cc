#include <iostream>
#include <vector>
using namespace std;

vector<int> tree;

int build(int node, int start, int end) {
	if (start == end)
		return tree[node] = 1;

	int mid = (start + end) / 2;
	int left = build(2 * node, start, mid);
	int right = build(2 * node + 1, mid + 1, end);

	return tree[node] = left + right;
}

//pos + 1 번째 사람 찾기
int query(int node, int start, int end, int K) {
	if (start == end)
		return start;

	int mid = (start + end) / 2;
	int left = tree[2 * node];

	if (left >= K)
		return query(node * 2, start, mid, K);
	else
		return query(node * 2 + 1, mid + 1, end, K - left);
}

int update(int node, int start, int end, int location) {
	if (location < start || location > end)
		return tree[node];
	if (start == end)
		return tree[node] = 0;

	int mid = (start + end) / 2;
	int left = update(2 * node, start, mid, location);
	int right = update(2 * node + 1, mid + 1, end, location);

	return tree[node] = left + right;
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	
	int N, K;
	cin >> N >> K;

	tree.resize(4*N);
	build(1, 0, N - 1);

	int pos = 0;
	int remain = N;

	cout << '<';
	for (int i = 0; i < N; i++) {
		pos = (pos + K - 1) % remain;

		int x = query(1, 0, N - 1, pos+1);
		update(1, 0, N - 1, x);

		remain--;
		cout << x+1;
		if (i != N - 1)
			cout << ", ";
	}
	cout << '>';
}