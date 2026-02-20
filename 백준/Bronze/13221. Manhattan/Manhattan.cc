#include <iostream>
using namespace std;


int main() {
	int x, y, t;
	cin >> x >> y >> t;

	int rx = 0 , ry = 0, dis = 201;
	for (int i = 0; i < t; i++) {
		int xx, yy;
		cin >> xx >> yy;
		int newdis = abs(x - xx) + abs(y - yy);
		if (newdis < dis) {
			rx = xx;
			ry = yy;
			dis = newdis;
		}
	}

	cout << rx << ' ' << ry << endl;
	return 0;
}