#include <iostream>
#include <string>
using namespace std;

int main() {
    string s;
    cin >> s;

    if (s.length() <= 2) {
        cout << "◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!";
        return 0;
    }

    int diff = s[0] - '0' - (s[1] - '0');
    for (int i = 2; i < s.length(); i++) {
        int curr = s[i - 1] - '0' - (s[i] - '0');
        if (diff != curr) {
            cout << "흥칫뿡!! <(￣ ﹌ ￣)>";
            return 0;
        }
    }

    cout << "◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!";
    return 0;
}