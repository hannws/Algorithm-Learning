#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>
using namespace std;
using ll = long long;
using pii = pair<ll, int>;

const pii INF = { LLONG_MAX, 100001 };
vector<pii> segtree;
vector<ll> A;

pii build(int start, int end, int node) {
    if (start == end)
        return segtree[node] = { A[start], start };

    int mid = (start + end) / 2;
    pii left = build(start, mid, 2 * node);
    pii right = build(mid + 1, end, 2 * node + 1);

    return segtree[node] = min(left, right);
}

pii query(int start, int end, int node, int b, int c) {
    if (end < b || start > c) {
        return INF;
    }

    if (b <= start && end <= c)
        return segtree[node];

    int mid = (start + end) / 2;
    pii left = query(start, mid, 2 * node, b, c);
    pii right = query(mid + 1, end, 2 * node + 1, b, c);
    return min(left, right);
}

void update(int start, int end, int node, int b, ll c) {
    if (b < start || b > end) {
        return;
    }
    
    if (start == end) {
        segtree[node] = { c, b };
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

    build(0, N-1, 1);

    cin >> Q;

    for (int i = 0; i < Q; i++) {
        ll a, b, c;
        cin >> a >> b >> c;
        if (a == 1)
            update(0, N-1, 1, b - 1, c);
        else
            cout << query(0, N-1, 1, b - 1, c - 1).second+1 << '\n';
    }
    return 0;
}