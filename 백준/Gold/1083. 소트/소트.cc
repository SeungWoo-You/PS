#include <iostream>

#define MAX_N 50
#define MIN(x, y) ((x < y) ? (x) : (y))

using namespace std;

int arr[MAX_N];

void swap(int *a, int *b) {
	int temp = *a;
	*a = *b;
	*b = temp;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	int N;
	cin >> N;

	for (int i = 0; i < N; i++)
		cin >> arr[i];

	int S;
	cin >> S;

	int idx = 0;

	while (idx < N && S > 0) {
		int max_idx = idx;

		for (int i = idx; i <= MIN(N - 1, idx + S); i++)
			if (arr[max_idx] < arr[i]) max_idx = i;

		for (int i = max_idx; i > idx; i--) {
			swap(&arr[i], &arr[i - 1]);
			S--;
		}

		idx++;
	}

	for (int i = 0; i < N; i++) cout << arr[i] << ' ';

	return 0;
}