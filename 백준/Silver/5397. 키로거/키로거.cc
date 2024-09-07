#include <iostream>
#include <list>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	int T;
	cin >> T;

	while (T--) {
		string S;
		cin >> S;

		list<char> ls;
		auto it = ls.end();

		for (char c : S) {
			if (c == '<') {
				if (it != ls.begin()) it--;
			}
			else if (c == '>') {
				if (it != ls.end()) it++;
			}
			else if (c == '-') {
				if (it != ls.begin())
					it = ls.erase(--it);
			}
			else
				it = ++ls.insert(it, c);
		}

		for (char c : ls) cout << c;
		cout << '\n';
	}

	return 0;
}