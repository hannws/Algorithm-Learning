#include <iostream>
#include <cctype>
using namespace std;


int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	char S;
	cin >> S;

	if (tolower(S) == 'n') {
		cout << "Naver D2" << endl;
	}
	else
		cout << "Naver Whale" << endl;

	return 0;
}