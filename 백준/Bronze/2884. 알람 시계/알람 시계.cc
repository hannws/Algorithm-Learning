#include <iostream>
#include <string>
using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	
	int H, M;
	cin >> H >> M;

	if (M >= 45) {
		M -= 45;
	} 
	else {
		H = (H == 0) ? 23 : H - 1;
		M += 15;
	}
	cout << H << " " << M << "\n";
	return 0;
}