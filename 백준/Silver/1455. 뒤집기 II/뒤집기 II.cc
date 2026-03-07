#include <iostream>
#include <vector>
#include <string>
using namespace std;

void change(vector<vector<int>>& v, int r, int c) {
    for (int i = 0; i <= r; i++) {
        for (int j = 0; j <= c; j++)
            v[i][j] = 1 - v[i][j];
    }
}

int main() {
    int N, M;
    cin >> N >> M;

    vector<vector<int>> grid(N, vector<int>(M));

    for (int i = 0; i < N; i++) {
        string s;
        cin >> s;
        for (int j = 0; j < M; j++)
            grid[i][j] = s[j] - '0';
    }

    int result = 0;

    for (int i = N - 1; i >= 0; i--) {
        for (int j = M - 1; j >= 0; j--) {
            if (grid[i][j] == 1) {
                change(grid, i, j);
                result++;
            }
        }
    }

    cout << result;
    return 0;
}