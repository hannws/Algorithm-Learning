#include <iostream>
#include <string>
using namespace std;

int main() {
    string L, R;
    cin >> L >> R;

    if (L.length() != R.length()) {
        cout << 0;
        return 0;
    }

    int result = 0;

    for (int i = 0; i < L.length(); i++) {
        if (L[i] != R[i])
            break;

        if (L[i] == '8')
            result++;
    }

    cout << result;
}