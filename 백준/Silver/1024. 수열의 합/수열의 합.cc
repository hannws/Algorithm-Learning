#include <iostream>
#include <vector>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, L;
    int start = -1;
    int end = -1;
    cin >> N >> L;

    while (L <= 100) {
        if (2 * N % L == 0) {
            if (2 * N / L - L + 1 < 0) {
                L++;
                continue;
            }

            if (((2 * N / L - L + 1) % 2) == 0) {
                start = (2 * N / L - L + 1) / 2;
                end = start + L - 1;
                break;
            }
        }
        L++;
    }

    for (int i = start; i <= end; i++) {
        cout << i << ' ';
    }

    return 0;
}
