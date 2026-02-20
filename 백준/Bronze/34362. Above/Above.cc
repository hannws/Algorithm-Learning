#include <iostream>
#include <iomanip>
using namespace std;


int main() {
	double altitude;
	cin >> altitude;

	cout << fixed << setprecision(5) << altitude - 0.3 << endl;
	return 0;
}