#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
using ll = long long;
using pii = pair<ll, ll>;

vector<pii> segtree;
vector<ll> A;

void build(int node, int l, int r) {
    if (l == r) {
        if (A[l] % 2 == 0) segtree[node] = { 1,0 };
        else segtree[node] = { 0, 1 };
        return;
    }

    int mid = (l + r) / 2;
    build(2*node, l, mid);
    build(2*node+1, mid+1, r);

    pii left = segtree[node * 2];
    pii right = segtree[node * 2 + 1];

    segtree[node] = { left.first + right.first, left.second + right.second };
}

pii query(int node, int l, int r, int i, int j) {
    if (r < i || l > j) {
        return { 0, 0 };
    }

    if (i <= l && r <= j)
        return segtree[node];

    int mid = (l + r) / 2;
    pii left = query(node * 2, l, mid, i, j);
    pii right = query(node * 2 + 1, mid + 1, r, i, j);
    return {left.first + right.first, left.second + right.second};
}

void update(int node, int l, int r, int j, int k) {
    if (r < j || l > j) {
        return;
    }

    if (l == r) {
        if (k % 2 == 0) {
            segtree[node] = { 1, 0 };
        }
        else {
            segtree[node] = { 0,1 };
        }
        return;
    }

    int mid = (l + r) / 2;
    update(node * 2, l, mid, j, k);
    update(node * 2+1, mid + 1, r, j, k);

    pii left = segtree[node * 2];
    pii right = segtree[node * 2 + 1];

    segtree[node] = { left.first + right.first, left.second + right.second };
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
        if (i == 2) {
            cout << query(1, 0, N - 1, j-1, k-1).first << '\n';
        }
        else if (i == 3) {
            cout << query(1, 0, N - 1, j-1, k-1).second << '\n';
        }
        else {
            update(1, 0, N - 1, j - 1, k);
        }
    }
    return 0;
}