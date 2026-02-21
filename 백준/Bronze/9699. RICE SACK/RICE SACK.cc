#include <iostream>
using namespace std;


int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int t;
	cin >> t;

	for(int i = 1; i<= t; i++) {
		int num,  max_val = 0;
		for (int j = 0; j < 5; j++) {
			cin >> num;
			max_val = max(num, max_val);
		}
		
		cout << "Case #" << i << ": " << max_val << '\n';
	}
	
	return 0;
}