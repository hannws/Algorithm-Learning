#include <iostream>
using namespace std;


int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int R, S;
	cin >> R >> S;

	cout << (R * 8 + S * 3 - 28) << endl;

	return 0;
}