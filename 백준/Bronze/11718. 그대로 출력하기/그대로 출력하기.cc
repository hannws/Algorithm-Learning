#include <iostream>
#include <string>
using namespace std;


int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	string N;
	while (getline(cin, N)) {
		cout << N << '\n';
	}

	return 0;
}