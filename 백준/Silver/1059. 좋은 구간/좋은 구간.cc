#include <iostream>

#define MAX_L 50

using namespace std;

int set[MAX_L] = {0};
int temps[MAX_L] = {0};

void counting_sort(int size, int exp) {
	int counts[10] = {0};

	for (int i = 0; i < size; i++) {
		int idx = (set[i] / exp) % 10;
		counts[idx]++;
	}

	for (int i = 1; i < 10; i++)
		counts[i] += counts[i - 1];

	for (int i = size - 1; i >= 0; i--) {
		int idx = (set[i] / exp) % 10;
		temps[--counts[idx]] = set[i];
	}

	for (int i = 0; i < size; i++)
		set[i] = temps[i];
}

void radix_sort(int size) {
	int max_elem = 0;

	for (int i = 0; i < size; i++)
		if (max_elem < set[i]) max_elem = set[i];

	for (int exp = 1; max_elem / exp > 0; exp *= 10)
		counting_sort(size, exp);

}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	int L;
	cin >> L;

	for (int i = 0; i < L; i++) cin >> set[i];

	int N;
	cin >> N;

	radix_sort(L);

	int lower = N, upper = 1;

	for (int i = 0; i < L; i++) {
		if (set[i] == N) {
			lower = 1, upper = 1;
			break;
		}
		else if (set[i] > N) {
			upper = set[i] - N;
			break;
		}
		else lower = N - set[i];
	}

	cout << (upper * lower - 1);

	return 0;
}