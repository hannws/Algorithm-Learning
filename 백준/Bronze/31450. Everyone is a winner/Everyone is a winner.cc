#include <iostream>
using namespace std;


int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int M, K;
	cin >> M >> K;

	if (M % K == 0) cout << "Yes" << '\n';
	else cout << "No" << '\n';

	return 0;
}