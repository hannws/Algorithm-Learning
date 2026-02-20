#include <iostream>
using namespace std;


int main() {
	int n;
	cin >> n;

	int result = 0;
	do {
		if (n / 100) {
			int num3, num2, num1;
			num3 = n / 100;
			num2 = (n % 100) / 10;
			num1 = n % 10;
			if (num3 - num2 == num2 - num1) result++;
		}
		else
			result++;
	} while (--n);

	cout << result << endl;
	return 0;
}