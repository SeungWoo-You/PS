#include <iostream>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	int T;
	cin >> T;

	while (T--) {
		int N;
		long long A, B;
		cin >> N >> A >> B;

		long long target = A > B ? B : A;
		int count = 0;

		while ((target & 1) == 0)
			count++, target >>= 1;

		cout << N - count << '\n';
	}

	return 0;
}