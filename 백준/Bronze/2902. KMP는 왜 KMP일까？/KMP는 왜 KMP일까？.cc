#include <iostream>
#include <string>
using namespace std;


int main() {
	string s;
	cin >> s;

	for (char c : s) {
		if (isupper(c))
			cout << c;
	}

	return 0;
}