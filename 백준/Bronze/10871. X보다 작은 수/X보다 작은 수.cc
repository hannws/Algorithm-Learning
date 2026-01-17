#include <iostream>
using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	
	int N, X;
	cin >> N >> X;
	for (int i = 1; i <= N; i++) {
		int num;
		cin >> num;
		if (num < X) {
			cout << num << " ";
		}
	}
	return 0;
}