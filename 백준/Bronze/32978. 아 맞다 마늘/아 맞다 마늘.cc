#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int N;
	cin >> N;

	vector<string> ingredient(N);
	for (string& i : ingredient)
		cin >> i;

	for (int i = 0; i < N - 1; i++) {
		string includeingre;
		cin >> includeingre;
		ingredient.erase(remove(ingredient.begin(), ingredient.end(), includeingre), ingredient.end());
	}

	for (string i : ingredient)
		cout << i;
	return 0;
}