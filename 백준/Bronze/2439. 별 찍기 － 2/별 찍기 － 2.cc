#include <iostream>
#include <iomanip>
#include <string>
using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	
	string s;
	int N;
	cin >> N;

	for (int i = 1; i<=N; i++) {
		s.assign(i, '*');
		cout << setw(N) << s << '\n';
	}

	return 0;
}