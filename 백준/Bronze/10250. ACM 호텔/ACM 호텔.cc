#include <iostream>
using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	
	int T;
	cin >> T;

	while(T--) {
		int H, W, N;
		cin >> H >> W >> N;
		
		int floor, room;

		if ((N % H) == 0) {
			floor = H * 100;
			room = N / H;
		}
		else {
			floor = (N % H) * 100;
			room = N / H + 1;
		}

		cout << floor + room << '\n';
	}
	return 0;
}