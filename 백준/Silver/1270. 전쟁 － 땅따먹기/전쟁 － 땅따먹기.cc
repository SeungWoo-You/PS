#include <iostream>
#include <unordered_map>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int n;
	cin >> n;

	while (n--) {
		int T;
		cin >> T;
		
		unordered_map<string, int> troops;

		for (int i = 0; i < T; i++) {
			string soldier;
			cin >> soldier;

			troops[soldier] += 1;
		}

		bool checked = false;

		for (auto& [k, v] : troops) {
			if (v > (T >> 1)) {
				cout << k << '\n';
				checked = true;
				break;
			}
		}
		if (!checked) cout << "SYJKGW\n";
	}

	return 0;
}