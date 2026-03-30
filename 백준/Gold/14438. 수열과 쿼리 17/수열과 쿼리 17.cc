#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>
using namespace std;
using ll = long long;

const ll INF = LLONG_MAX;
vector<ll> segtree;
vector<ll> A;

ll build(int start, int end, int node) {
    if (start == end)
        return segtree[node] = A[start];

    int mid = (start + end) / 2;
    ll left = build(start, mid, 2 * node);
    ll right = build(mid + 1, end, 2 * node + 1);

    return segtree[node] = min(left, right);
}

ll query(int start, int end, int node, int b, int c) {
    if (end < b || start > c) {
        return INF;
    }

    if (b <= start && end <= c)
        return segtree[node];

    int mid = (start + end) / 2;
    ll left = query(start, mid, 2 * node, b, c);
    ll right = query(mid + 1, end, 2 * node + 1, b, c);
    return min(left, right);
}

void update(int start, int end, int node, int b, ll c) {
    if (b < start || b > end) {
        return;
    }

    if (start == end) {
        segtree[node] = c;
        return;
    }

    int mid = (start + end) / 2;
    update(start, mid, 2 * node, b, c);
    update(mid + 1, end, 2 * node + 1, b, c);
    segtree[node] = min(segtree[2 * node], segtree[2 * node + 1]);
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

    build(0, N - 1, 1);

    cin >> Q;

    for (int i = 0; i < Q; i++) {
        ll a, b, c;
        cin >> a >> b >> c;
        if (a == 1)
            update(0, N - 1, 1, b - 1, c);
        else
            cout << query(0, N - 1, 1, b - 1, c - 1) << '\n';
    }
    return 0;
}