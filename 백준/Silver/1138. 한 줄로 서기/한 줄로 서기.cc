#include <iostream>
#include <vector>
using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int N;
	cin >> N;

	vector<int> line(N), result(N, 0);
	for (int& i : line)
		cin >> i;

	for (int i = 0; i < N; i++) {
		int cnt = 0;
		for (int j = 0; j < N; j++) {
			if (result[j] == 0) {
				if(cnt == line[i]){
					result[j] = i + 1;
					break;
				}
				cnt++;
			}
		}
	}

	for (const auto& i : result)
		cout << i << ' ';

	return 0;
}