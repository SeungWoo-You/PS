#include <iostream>
#include <unordered_set>
#include <unordered_map>
#include <string>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int scenario = 1;

	while (true) {
		int n;
		cin >> n;
		cin.ignore();

		if (n == 0) break;

		unordered_map<int, string> girls;
		unordered_set<string> checked;

		for (int i = 1; i <= n; i++) {
			string name;
			getline(cin, name);

			girls[i] = name;
		}

		for (int i = 0; i < 2 * n - 1; i++) {
			int id;
			string _;
			cin >> id >> _;

			if (checked.count(girls[id])) checked.erase(girls[id]);
			else checked.insert(girls[id]);
		}

		for (string last : checked) cout << scenario << ' ' << last << '\n';

		scenario += 1;
	}

	return 0;
}