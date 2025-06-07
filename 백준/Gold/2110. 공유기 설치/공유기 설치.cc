#include <iostream>

#define MAX_N 200'000
#define MAX_X 1'000'000'000

using namespace std;

int houses[MAX_N], temps[MAX_N];

void counting_sort(int N, int exp) {
	int counts[10] = {0};
	
	for (int i = 0; i < N; i++) {
		int idx = (houses[i] / exp) % 10;
		counts[idx]++;
	}

	for (int i = 1; i < 10; i++)
		counts[i] += counts[i - 1];

	for (int i = N - 1; i >= 0; i--) {
		int idx = (houses[i] / exp) % 10;
		temps[--counts[idx]] = houses[i];
	}

	for (int i = 0; i < N; i++)
		houses[i] = temps[i];
}

void radix_sort(int N) {
	int max_elem = 0;

	for (int i = 0; i < N; i++)
		if (max_elem < houses[i]) max_elem = houses[i];

	for (int exp = 1; max_elem / exp > 0; exp *= 10)
		counting_sort(N, exp);
}

int place_wifis(int N, int C) {
	int left = 0, right = MAX_X;
	int res = -1;

	while (left <= right) {
		int mid = (left + right) >> 1;
		int count = 1;
		int prev_house = houses[0];

		for (int i = 1; i < N; i++)
			if (houses[i] - prev_house >= mid)
				count++, prev_house = houses[i];

		if (count >= C) left = mid + 1, res = mid;
		else right = mid - 1;
	}

	return res;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	int N, C;
	cin >> N >> C;

	for (int i = 0; i < N; i++)
		cin >> houses[i];

	radix_sort(N);

	cout << place_wifis(N, C);

	return 0;
}