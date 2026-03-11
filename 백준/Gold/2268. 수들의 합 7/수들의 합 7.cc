#include <iostream>
#include <vector>
using namespace std;

vector<long long> tree;

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

void update(int node, int start, int end, int a, int b) {
    if (a < start || a > end)
        return;

    if (start == end) {
        tree[node] = b;
        return;
    }       


    int mid = (start + end) / 2;

    update(node * 2, start, mid, a, b);
    update(node * 2 + 1, mid + 1, end, a, b);

    tree[node] = tree[node*2] + tree[node*2 + 1];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M;
    cin >> N >> M;

    tree.resize(4 * N);

    for (int i = 0; i < M; i++) {
        int q, a, b;
        cin >> q;
        if (q == 0) {
            cin >> a >> b;
            cout << query(1, 0, N - 1, min(a, b) - 1, max(a, b) - 1) << '\n';
        }
        else if(q == 1) {
            cin >> a >> b;
            update(1, 0, N - 1, a - 1, b);
        }
    }
    return 0;
}