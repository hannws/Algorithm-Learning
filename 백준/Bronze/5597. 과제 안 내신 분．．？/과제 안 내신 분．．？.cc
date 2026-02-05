#include <iostream>
#include <vector>
using namespace std;


int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int num;
	int minst = 29, maxst = 0;
	vector<int> student(30, 1);
	for (int i = 0; i < 28; i++) {
		cin >> num;
		student[num - 1] = 0;
	}

	for (int i = 0; i < 30; i++) {
		if (student[i] == 1) {
			if (minst > i) minst = i;
			else if (maxst < i) maxst = i;
		}
	}

	cout << minst + 1 << '\n';
	cout << maxst + 1 << '\n';
	return 0;
}