#include <iostream>
#define FASTIO ios::sync_with_stdio(0), cin.tie(0), cout.tie(0)

using namespace std;

#define NATURAL_SUM(N) ((N) * (N + 1) / 2)

int main() {
	FASTIO;

	long long N, sum = 0;

	cin >> N;

	for (int i = 0; i < N; i++) {
		int num;

		cin >> num;
		sum += num;
	}

	cout << sum - NATURAL_SUM(N - 1);

	return 0;
}