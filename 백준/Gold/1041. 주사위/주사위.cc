#include <iostream>
#include <algorithm>
#include <climits>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long N;
    cin >> N;

    long long dice[6];
    for (auto& i : dice) {
        cin >> i;
    }

    if (N == 1) {
        long long sum = 0;
        long long mx = 0;
        for (int i = 0; i < 6; i++) {
            sum += dice[i];
            mx = max(mx, dice[i]);
        }
        cout << sum - mx;
        return 0;
    }

    long long min1 = LLONG_MAX;
    for (int i = 0; i < 6; i++) {
        min1 = min(min1, dice[i]);
    }

    long long min2 = LLONG_MAX;
    for (int i = 0; i < 5; i++) {
        for (int j = i + 1; j < 6; j++) {
            if (j + i == 5) continue;
            min2 = min(min2, dice[i] + dice[j]);
        }
    }

    long long min3 = LLONG_MAX;
    for (int i = 0; i < 4; i++) {
        for (int j = i + 1; j < 5; j++) {
            if (i + j == 5) continue;
            for (int k = j + 1; k < 6; k++) {
                if (i + k == 5 || j + k == 5) continue;
                min3 = min(min3, dice[i] + dice[j] + dice[k]);
            }
        }
    }

    long long count3 = 4;
    long long count2 = 4 * (2 * N - 3);
    long long count1 = (N - 2) * (N - 2) * 5 + (N - 2) * 4;

    long long result = min1 * count1 + min2 * count2 + min3 * count3;
    cout << result;

    return 0;
}
