#include <iostream>
#include <iomanip>
using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	int A, B;
	cin >> A >> B;

	int arr[1000] = { 0 };
	int x = A / B;
	int N = A % B;

	for (int i = 0; i < 1000; i++) {
		arr[i] = (N * 10) / B;
		N = (N * 10) % B;
	}
	cout << x << '.';
	for (const auto& i : arr)
		cout << i;
	return 0;
}