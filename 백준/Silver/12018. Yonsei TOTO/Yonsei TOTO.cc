#include <iostream>

#define MAX_P 100
#define MAX_N 100

using namespace std;

int mileages[MAX_P];
int temps[MAX_P];

void counting_sort(int arr[], int N, int exp) {
	int counts[10] = {0};

	for (int i = 0; i < N; i++) {
		int idx = (arr[i] / exp) % 10;
		counts[idx]++;
	}

	for (int i = 1; i < 10; i++)
		counts[i] += counts[i - 1];

	for (int i = N - 1; i >= 0; i--) {
		int idx = (arr[i] / exp) % 10;
		temps[--counts[idx]] = arr[i];
	}

	for (int i = 0; i < N; i++)
		arr[i] = temps[i];
}

void radix_sort(int arr[], int N) {
	int max_elem = 0;

	for (int i = 0; i < N; i++)
		if (max_elem < arr[i]) max_elem = arr[i];

	for (int exp = 1; max_elem / exp > 0; exp *= 10)
		counting_sort(arr, N, exp);
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	int N, M;
	int targets[MAX_N] = {0};
	int msize = 0;

	cin >> N >> M;

	for (int i = 0; i < N; i++) {
		int P, L;
		cin >> P >> L;

		for (int i = 0; i < P; i++)
			cin >> mileages[i];

		if (P < L)
			targets[msize++] = 1;
		else {
			radix_sort(mileages, P);
			targets[msize++] = mileages[P - L];
		}
	}
	
	radix_sort(targets, N);

	int answer = 0;

	for (int i = 0, used = 0; i < N; i++) {
		if (used + targets[i] > M) break;
		answer++, used += targets[i];
	}
		
	cout << answer;

	return 0;
}