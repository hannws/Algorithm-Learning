#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;


int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int N;
	cin >> N;
	vector<int> arr(N);
	for (int i = 0; i < N; i++) {
		cin >> arr[i];
	}
	int M;
	cin >> M;

	int result = count(arr.begin(), arr.end(), M);
	cout << result << endl;
	return 0;
}