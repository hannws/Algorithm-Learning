#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <map>
#include <iomanip>
using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	
	int totalcredit = 0;
	double totalgrade=0.0;

	map<string, double> gtos = {
		{"A+",4.5},
		{"A0", 4.0},
		{"B+", 3.5},
		{"B0", 3.0},
		{"C+", 2.5},
		{"C0", 2.0},
		{"D+", 1.5},
		{"D0", 1.0},
		{"F", 0.0},
		{"P", -1}
	};

	string course, grade;
	double credit;
	for (int i = 0; i < 20; i++) {
		cin >> course >> credit >> grade;
		if (gtos[grade] != -1) {
			totalcredit += credit;
			totalgrade += gtos[grade] * credit;
		}
	}
	
	cout << fixed << setprecision(6) << totalgrade / totalcredit << '\n';
}