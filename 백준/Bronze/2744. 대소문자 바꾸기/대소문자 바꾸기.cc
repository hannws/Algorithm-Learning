#include <iostream>
#include <string>
#include <cctype>
using namespace std;


int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	string n;
	cin >> n;

	for (int i = 0; i < n.length(); i++) {
		if (isupper(n[i])) {
			n[i] = tolower(n[i]);
		}
		else {
			n[i] = toupper(n[i]);
		}
	}

	cout << n << endl;

	return 0;
}