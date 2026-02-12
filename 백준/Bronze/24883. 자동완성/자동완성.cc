#include <iostream>
#include <string>
#include <unordered_map>
using namespace std;


int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	string S;
	cin >> S;

	unordered_map<string, string> um = { {"N", "Naver D2"}, {"whale", "Naver Whale"} };

	if (S == "n" || S == "N") {
		cout << um["N"] << endl;
	}
	else
		cout << um["whale"] << endl;
	return 0;
}