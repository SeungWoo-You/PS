#include <iostream>
#include <numeric>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int T;
	cin >> T;

	while (T--) {
		int M, N, x, y;
		cin >> M >> N >> x >> y;

		int max_year = lcm(M, N);
		int result = -1;

		for (int yr = x; yr <= max_year; yr += M) {
			int n = yr % N;
			if (n == 0) n = N;

			if (n == y) {
				result = yr;
				break;
			}
		}

		cout << result << '\n';
	}

	return 0;
}