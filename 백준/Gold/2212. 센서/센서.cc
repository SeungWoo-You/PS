#include <iostream>

#define MAX_N 10'000

using namespace std;

int negs[MAX_N] = {0};
int poss[MAX_N] = {0};
int temps[MAX_N];
int gaps[MAX_N - 1] = {0};

void counting_sort(int arr[], int size, int place) {
	int counts[10] = {0};

	for (int i = 0; i < size; i++) {
		int idx = (arr[i] / place) % 10;
		counts[idx]++;
	}

	for (int i = 1; i < 10; i++)
		counts[i] += counts[i - 1];

	for (int i = size - 1; i >= 0; i--) {
		int idx = (arr[i] / place) % 10;
		--counts[idx];
		temps[counts[idx]] = arr[i];
	}

	for (int i = 0; i < size; i++)
		arr[i] = temps[i];
}

void radix_sort(int arr[], int size) {
	int max_val = 0;
	
	for (int i = 0; i < size; i++)
		if (max_val < arr[i]) max_val = arr[i];

	for (int place = 1; max_val / place > 0; place *= 10)
		counting_sort(arr, size, place);
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	int N, K;
	cin >> N >> K;

	int neg_N = 0, pos_N = 0;

	for (int i = 0; i < N; i++) {
		int x;
		cin >> x;

		if (x >= 0) poss[pos_N++] = x;
		else negs[neg_N++] = -x;
	}

	if (K >= N) {
		cout << 0;

		return 0;
	}

	radix_sort(poss, pos_N);
	radix_sort(negs, neg_N);

	int gsize = 0;

	for (int i = 0; i < neg_N - 1; i++)
		gaps[gsize++] = negs[i + 1] - negs[i];

	if (pos_N > 0 && neg_N > 0)
		gaps[gsize++] = poss[0] + negs[0];

	for (int i = 0; i < pos_N - 1; i++)
		gaps[gsize++] = poss[i + 1] - poss[i];
		
	radix_sort(gaps, gsize);

	int total = 0;

	for (int i = 0; i <= N - 1 - K; i++)
		total += gaps[i];

	cout << total;

	return 0;
}