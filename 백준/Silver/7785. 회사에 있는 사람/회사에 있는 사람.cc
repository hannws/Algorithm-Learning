#include <iostream>
#include <set>
using namespace std;


int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	
	int n;
	cin >> n;

	set<string> s;

	while (n--) {
		string name, log;
		cin >> name >> log;

		if (log == "enter")
			s.insert(name);
		else
			s.erase(name);
	}

	for (auto it = s.rbegin(); it != s.rend(); it++)
		cout << *it << '\n';

	return 0;
}