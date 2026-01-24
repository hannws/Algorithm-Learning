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

	int N, T, P;
	cin >> N;

	vector<int> people(6);
	for (int& p : people) {
		cin >> p;
	}

	cin >> T >> P;
	int shirtbundle = 0;
	for (int a : people) {
		shirtbundle += (a+T-1) / T;
	}

	int penbundle, pen;
	penbundle = N / P;
	pen = N % P;

	cout << shirtbundle << '\n';
	cout << penbundle << " " << pen << endl;

	return 0;
}