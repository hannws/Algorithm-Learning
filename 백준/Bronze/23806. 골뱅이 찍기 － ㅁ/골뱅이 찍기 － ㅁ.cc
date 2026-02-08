#include <iostream>
#include <string>
using namespace std;


int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int N;
	cin >> N;
	string top = "@", mid ="@";
	for (int i = 1; i < N * 5; i++) {
		top += "@";
	}
	for (int i = 1; i < 1 * N; i++) {
		mid += "@";
	}
	for (int i = 0; i < 3 * N; i++) {
		mid += " ";
	}
	for (int i = 0; i < 1 * N; i++) {
		mid += "@";
	}

	for (int i = 0; i < N; i++) {
		cout << top << '\n';
	}
	for (int i = 0; i < N * 3; i++) {
		cout << mid << '\n';
	}
	for (int i = 0; i < N; i++) {
		cout << top << '\n';
	}
	return 0;

}