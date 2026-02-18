#include <iostream>
#include <vector>
#include <string>
using namespace std;

const int MAX_K = 1000001;
bool is_prime[MAX_K];
vector<int> primes;

void sieve(int k) {
    fill(is_prime, is_prime + k, true);
    is_prime[0] = is_prime[1] = false;
    for (int i = 2; i < k; i++) {
        if (is_prime[i]) {
            primes.push_back(i);
            for (int j = i * 2; j < k; j += i)
                is_prime[j] = false;
        }
    }
}

bool div(string p, int n) {
    int remainder = 0;
    for (int i = 0; i < p.length(); i++) {
        remainder = (remainder * 10 + (p[i] - '0')) % n;
    }
    return remainder == 0;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string p;
    int k;
    cin >> p >> k;
    
    sieve(k);

    int answer = -1;

    for (int val : primes) {
        if (div(p, val)) {
            answer = val;
            break;
        }
    }

    if (answer == -1) {
        cout << "GOOD" << endl;
    }
    else {
        cout << "BAD " << answer << endl;
    }
    return 0;
}
