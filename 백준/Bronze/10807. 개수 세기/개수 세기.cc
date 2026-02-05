#include <iostream>
#include <vector>
using namespace std;


int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int N;
	cin >> N;
	vector<int> arr(N,0);
	for (int i = 0; i < N; i++) {
		cin >> arr[i];
	}
	int M;
	cin >> M;

	int result = 0;
	for (int i = 0; i < N; i++) {
		if (arr[i] == M) {
			result += 1;
		}
	}
	cout << result << endl;
	return 0;
}