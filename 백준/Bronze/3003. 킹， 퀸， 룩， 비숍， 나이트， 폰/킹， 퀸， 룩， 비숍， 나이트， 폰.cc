#include <iostream>
using namespace std;


int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int k, q, r, b, knight, pawn;
	cin >> k >> q >> r >> b >> knight >> pawn;
	cout << 1 - k << ' ' << 1 - q << ' ' << 2 - r << ' ' << 2 - b << ' ' << 2 - knight << ' ' << 8 - pawn << endl;
	return 0;
}