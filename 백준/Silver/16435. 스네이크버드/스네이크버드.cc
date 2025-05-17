#include <iostream>

#define MAX_N 1000

using namespace std;

int arr[MAX_N] = {0};
int temp_arr[MAX_N] = {0};

void counting_sort(int N, int exp) {
	int counts[10] = {0};

	for (int i = 0; i < N; i++) {
		int idx = (arr[i] / exp) % 10;
		counts[idx]++;
	}

	for (int i = 1; i < 10; i++)
		counts[i] += counts[i - 1];

	for (int i = N - 1; i >= 0; i--) {
		int idx = (arr[i] / exp) % 10;
		temp_arr[--counts[idx]] = arr[i];
	}

	for (int i = 0; i < N; i++)
		arr[i] = temp_arr[i];
}

void radix_sort(int N) {
	int max_elem = 0;

	for (int i = 0; i < N; i++)
		if (max_elem < arr[i]) max_elem = arr[i];

	for (int exp = 1; max_elem / exp > 0; exp *= 10)
		counting_sort(N, exp);
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	int N, L;
	cin >> N >> L;

	for (int i = 0; i < N; i++)
		cin >> arr[i];

	radix_sort(N);

	if (arr[N - 1] <= L) {
		cout << L + N;
		return 0;
	}

	for (int i = 0; i < N; i++, L++)
		if (arr[i] > L) break;

	cout << L;

	return 0;
}