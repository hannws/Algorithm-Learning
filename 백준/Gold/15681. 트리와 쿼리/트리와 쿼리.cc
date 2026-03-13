#include <iostream>
#include <vector>
using namespace std;

vector<int> subtree;
vector<vector<int>> connect;

void makesubtree(int node, int parent) {
    int cnt = 1;
    for (int x : connect[node]) {
        if (x == parent)
            continue;

        makesubtree(x, node);
        cnt += subtree[x];
    }
    subtree[node] = cnt;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, r, q;
    cin >> n >> r >> q;

    subtree.resize(n);
    connect.resize(n);

    for (int i = 0; i < n-1; i++) {
        int a, b;
        cin >> a >> b;
        connect[a-1].push_back(b-1);
        connect[b-1].push_back(a-1);
    }

    makesubtree(r - 1, -1);

    for (int i = 0; i < q; i++) {
        int Q;
        cin >> Q;

        cout << subtree[Q - 1] << '\n';
    }
    return 0;
}