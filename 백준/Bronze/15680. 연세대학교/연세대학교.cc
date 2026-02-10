#include <iostream>
#include <unordered_map>
#include <string>
using namespace std;


int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	unordered_map<int, string> um;
	um[0] = "YONSEI";
	um[1] = "Leading the Way to the Future";

	int N;
	cin >> N;

	cout << um[N] << endl;
	return 0;
}