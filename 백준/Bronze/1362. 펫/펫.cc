#include <iostream>
#include <string>
using namespace std;


int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int o, w, cnt = 1;

	while (cin >> o >> w && (o != 0 || w != 0)) {
		string act;
		int diff;
		bool die = false;

		while (cin >> act >> diff && (act != "#" || diff != 0)) {
			if (!die) {
				if (act == "F") w += diff;
				else if (act == "E") w -= diff;

				if (w <= 0) {
					die = true;
				}
			}
		}

		cout << cnt << ' ';
		if (die) {
			cout << "RIP" << '\n';
		}
		else {
			cout << ((w > (float)o / 2 && w < 2 * o) ? ":-)\n" : ":-(\n");
		}

		cnt++;
	}

	return 0;
}