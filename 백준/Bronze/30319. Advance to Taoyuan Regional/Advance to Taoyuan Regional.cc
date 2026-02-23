#include <iostream>
#include <string>
using namespace std;


int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	
	string s;
	cin >> s;

	int year, month, day;
	year = stoi(s.substr(0, 4));
	month = stoi(s.substr(5, 2));
	day = stoi(s.substr(8, 2));

	if (month >= 10) {
		cout << "TOO LATE";
	}
	else if (month == 9 && day > 16)
		cout << "TOO LATE";
	else
		cout << "GOOD";

	return 0;
}