#include <iostream>
using namespace std;


int main() {
	int t, person = 0;
	cin >> t;

	while (t--) {
		int s, c, a, r;
		cin >> s >> c >> a >> r;
		if (s >= 1000 || c >= 1600 || a >= 1500) {
			person++;
		}
		else if (r <= 30 && r != -1)
			person++;
	}

	cout << person << endl;
	return 0;
}