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
        int a;
        cin >> a;
        if (a == 1) {
            ll b, c;
            cin >> b >> c;
            update(0, N - 1, 1, b - 1, c);
        }
        else
            cout << segtree[1].second + 1 << '\n';
    }
    return 0;
}