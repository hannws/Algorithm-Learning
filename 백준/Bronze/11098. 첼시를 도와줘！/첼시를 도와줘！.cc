#include <iostream>
#include <string>
using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int test;
	cin >> test;

	int p, currprice, price;
	string currmember, member;
	while (test--) {
		cin >> p;
		currprice = 0;
		currmember = "";
		for (int i = 0; i < p; i++) {
			cin >> price >> member;
			if (price > currprice) {
				currprice = price;
				currmember = member;
			}
		}
		cout << currmember << '\n';
	}
	return 0;
}