#include <iostream>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	while (true) {
		int N, M;
		cin >> N >> M;
		
		if (cin.eof()) break;

		int count = 0;

		for (int n = N; n <= M; n++) {
			bool checked[10] = {false};
			bool passed = true;

			for (int exp = 1; n / exp > 0; exp *= 10) {
				int idx = (n / exp) % 10;

				if (checked[idx]) {
					passed = false;
					break;
				}

				checked[idx] = true;
			}

			if (passed) count++;
		}

		cout << count << '\n';
	}

	return 0;
}