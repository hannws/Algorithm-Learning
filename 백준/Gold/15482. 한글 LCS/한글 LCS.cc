#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

vector<string> split_utf8(const string& s) {
    vector<string> result;
    for (int i = 0; i < s.size(); i += 3) {
        result.push_back(s.substr(i, 3));
    }
    return result;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s1, s2;
    cin >> s1 >> s2;

    vector<string> a = split_utf8(s1);
    vector<string> b = split_utf8(s2);

    int n = a.size();
    int m = b.size();

    vector<vector<int>> dp(n + 1, vector<int>(m + 1, 0));

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
            if (a[i - 1] == b[j - 1])
                dp[i][j] = dp[i - 1][j - 1] + 1;
            else
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
        }
    }

    cout << dp[n][m] << '\n';

    return 0;
}