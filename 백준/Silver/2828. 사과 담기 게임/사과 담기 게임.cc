#include <iostream>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	int N, M, J;
	cin >> N >> M >> J;

	int left = 1, right = M;
	int count = 0;

	for (int i = 0; i < J; i++) {
		int pos;
		cin >> pos;

		if (pos < left) {
			int diff = left - pos;
			left -= diff, right -= diff;
			count += diff;
		}
		else if (pos > right) {
			int diff = pos - right;
			left += diff, right += diff;
			count += diff;
		}
	}

	cout << count;

	return 0;
}