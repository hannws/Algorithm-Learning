#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
using ll = long long;

vector<vector<ll>> segtree;
vector<ll> A;

void build(int node, int l, int r) {
    if (l == r) {
        segtree[node] = { A[l] };
        return;
    }

    int mid = (l + r) / 2;
    build(2*node, l, mid);
    build(2*node+1, mid+1, r);

    auto& left = segtree[node * 2];
    auto& right = segtree[node * 2 + 1];

    segtree[node].resize(left.size()+right.size());
    merge(left.begin(), left.end(), right.begin(), right.end(), segtree[node].begin());
}

ll query(int node, int l, int r, int i, int j, int k) {
    if (r < i || l > j) {
        return 0;
    }

    if (i <= l && r <= j)
        return segtree[node].end() - upper_bound(segtree[node].begin(), segtree[node].end(), k);

    int mid = (l + r) / 2;
    return query(node * 2, l, mid, i, j, k) + query(node * 2 + 1, mid + 1, r, i, j, k);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, Q;
    cin >> N;

    segtree.resize(4 * N);
    A.resize(N);

    for (ll& i : A) {
        cin >> i;
    }

    build(1, 0, N - 1);

    cin >> Q;

    while (Q--) {
        ll i, j, k;
        cin >> i >> j >> k;
        cout << query(1, 0, N - 1, i-1, j-1, k) << '\n';
    }
    return 0;
}