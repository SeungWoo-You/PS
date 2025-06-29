#include <iostream>

#define MAX_N 500'000
#define ABS(x) (((x) > 0) ? (x) : -(x))

using namespace std;

int ranks[MAX_N], temps[MAX_N];

void counting_sort(int exp, int N) {
	int counts[10] = {0};

	for (int i = 0; i < N; i++) {
		int idx = (ranks[i] / exp) % 10;
		counts[idx]++;
	}

	for (int i = 1; i < 10; i++)
		counts[i] += counts[i - 1];

	for (int i = N - 1; i >= 0; i--) {
		int idx = (ranks[i] / exp) % 10;
		temps[--counts[idx]] = ranks[i];
	}

	for (int i = 0; i < N; i++)
		ranks[i] = temps[i];
}

void radix_sort(int N) {
	int max_elem = 0;

	for (int i = 0; i < N; i++)
		if (max_elem < ranks[i]) max_elem = ranks[i];

	for (int exp = 1; max_elem / exp > 0; exp *= 10)
		counting_sort(exp, N);
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	int N;
	cin >> N;

	for (int i = 0; i < N; i++) cin >> ranks[i];

	radix_sort(N);

	long long res = 0;

	for (int i = 0; i < N; i++)
		res += (long long) ABS(i + 1 - ranks[i]);

	cout << res;

	return 0;
}