#include <iostream>
#include <string>
#include <list>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	string S;
	cin >> S;
	
	int M;
	cin >> M;

	list<char> ls;
	for (char c : S) ls.push_back(c);

	auto it = ls.end();

	while (M--) {
		char cmd;
		cin >> cmd;

		if (cmd == 'L') {
			if (it != ls.begin()) it--;
		}
		else if (cmd == 'D') {
			if (it != ls.end()) it++;
		}
		else if (cmd == 'B') {
			if (it != ls.begin())
				it = ls.erase(--it);
		}
		else if (cmd == 'P') {
			char c;
			cin >> c;
			it = ++ls.insert(it, c);
		}
	}

	for (auto c : ls) cout << c;

	return 0;
}