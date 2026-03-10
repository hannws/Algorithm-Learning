#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main() {
    int R, C, A, B;
    cin >> R >> C >> A >> B;

    for (int i = 0; i < R; i++) {
        for (int j = 0; j < A; j++) {
            for (int k = 0; k < C; k++) {
                for (int n = 0; n < B; n++) {
                    if ((k+i) % 2 == 0) {
                        cout << 'X';
                    }
                    else
                        cout << '.';
                }
            }
            cout << '\n';
        }
    }
}