#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int test;
	cin >> test;

	vector<int> now(3, 0), mini(3, 2020), maxi(3, -1);
	string name, minname, maxname;


	while (test--) {
		cin >> name >> now[2] >> now[1] >> now[0];
		if (now < mini) {
			mini = now;
			minname = name;
		}
		if (now > maxi) {
			maxi = now;
			maxname = name;
		}
	}
	cout << maxname << '\n';
	cout << minname << endl;

	return 0;
}