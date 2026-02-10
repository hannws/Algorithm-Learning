#include <iostream>
using namespace std;


int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int N;
	cin >> N;

	cout << (N * 78) / 100 << ' ' << (N * 80) / 100 + ((N * 20) / 100) * 78 / 100 << endl;
	return 0;
}