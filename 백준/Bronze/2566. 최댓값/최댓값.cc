#include <iostream>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	int max_val = -1;
	int x = -1, y = -1;

	for (int i = 1; i <= 9; i++)
		for (int j = 1; j <= 9; j++) {
			int val;
			cin >> val;

			if (val > max_val) {
				max_val = val;
				x = i, y = j;
			}
		}

	cout << max_val << '\n';
	cout << x << ' ' << y;

	return 0;
}