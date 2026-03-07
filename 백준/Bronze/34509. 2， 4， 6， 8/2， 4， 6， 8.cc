#include <iostream>
using namespace std;

int main() {
    int result = 0;

    for (int i = 10; i < 100; i++) {
        if (i % 10 == 8 || i / 10 == 8)
            continue;

        int num = (i % 10)*10 + i / 10;
        if (num % 4 != 0)
            continue;
        
        if ((num % 10 + num / 10) % 6 != 0)
            continue;

        result = i;
        break;
    }

    cout << result;
}