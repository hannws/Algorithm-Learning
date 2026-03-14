#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	string s1, s2, s3;
	cin >> s1 >> s2 >> s3;

	int n = s1.size();
	int m = s2.size();
	int x = s3.size();

	vector < vector<vector<int>>> dp(n + 1, vector<vector<int>>(m + 1, vector<int>(x + 1, 0)));

	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= m; j++) {
			for (int k = 1; k <= x; k++) {
				if (s1[i - 1] == s2[j - 1] && s2[j-1] == s3[k - 1])
					dp[i][j][k] = dp[i - 1][j - 1][k - 1] + 1;
				else
					dp[i][j][k] = max({ dp[i - 1][j][k], dp[i][j - 1][k], dp[i][j][k - 1] });
			}
		}
	}

	cout << dp[n][m][x];
	return 0;
}