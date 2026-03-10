#include <iostream>
#include <vector>
using namespace std;

vector<long long> tree;
vector<long long> nums;

long long build(int node, int start, int end) {
    if (start == end)
        return tree[node] = nums[start];

    int mid = (start + end) / 2;
    long long left = build(node * 2, start, mid);
    long long right = build(node * 2 + 1, mid + 1, end);
    
    return tree[node] = left + right;
}

long long query(int node, int start, int end, int a, int b) {
    if ((start > b) || (end < a))
        return 0;

    if ((start >= a) && (end <= b))
        return tree[node];

    int mid = (start + end) / 2;
    long long left = query(node * 2, start, mid, a, b);
    long long right = query(node * 2 + 1, mid + 1, end, a, b);

    return left + right;
}

long long update(int node, int start, int end, int a, long long b) {
    if (start > a || end < a)
        return tree[node];

    if (start == end)
        return tree[node] = b;


    int mid = (start + end) / 2;
    long long left = update(node * 2, start, mid, a, b);
    long long right = update(node * 2 + 1, mid + 1, end, a, b);

    return tree[node] = left + right;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, Q;
    cin >> N >> Q;
    tree.resize(N * 4);
    nums.resize(N);

    for (long long& i : nums)
        cin >> i;

    build(1, 0, N - 1);

    for (int i = 0; i < Q; i++) {
        int a, b;
        cin >> a >> b;
        cout << query(1, 0, N - 1, min(a, b) - 1, max(a, b) - 1) << '\n';

        cin >> a >> b;
        update(1, 0, N - 1, a - 1, b);
    }
}