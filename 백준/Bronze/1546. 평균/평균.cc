#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int N;
	cin >> N;

	double total = 0;
	vector<int> score(N, 0);
	for (int i = 0; i < N; i++) {
		cin >> score[i];
		total += score[i];
	}

	int M = *max_element(score.begin(), score.end());
	
	double result = ((total * 100.0) / M) / N;

	cout.precision(6);
	cout << fixed;
	cout << result << endl;

	return 0;
}