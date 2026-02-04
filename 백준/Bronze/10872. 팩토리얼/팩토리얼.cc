#include <iostream>
using namespace std;


int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	long long N;
	cin >> N;
	long long fact = 1;
	for (int i = 1; i <= N; i++) {
		fact *= i;
	}
	cout << fact << endl;
	return 0;
}