#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, M, q;
    cin >> N >> M >> q;

    vector<vector<int>> grid(N, vector<int>(M));
    for (int i = 0; i < N; i++)
        for (int j = 0; j < M; j++)
            cin >> grid[i][j];

    vector<int> row(N);
    for (int i = 0; i < N; i++)
        row[i] = i;

    while (q--) {
        int query;
        cin >> query;

        if (query == 0) {
            int i, j, k;
            cin >> i >> j >> k;
            grid[row[i]][j] = k;
        }
        else {
            int i, j;
            cin >> i >> j;
            swap(row[i], row[j]);
        }
    }

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++)
            cout << grid[row[i]][j] << ' ';
        cout << '\n';
    }

    return 0;
}
