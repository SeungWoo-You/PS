#include <iostream>

#define MAX_N 200'000
#define MAX_X 1'000'000'000

using namespace std;

int houses[MAX_N];

void swap(int* x, int* y) {
	int temp = *x;
	*x = *y;
	*y = temp;
}

int get_pivot_idx(int left, int right) {
	int mid = (left + right) >> 1;
	int a = houses[left];
	int b = houses[mid];
	int c = houses[right];

	if ((a > b && a < c) || (a < b && a > c))
		swap(&houses[left], &houses[left]);
	else if ((b > a && b < c) || (b < a && b > c))
		swap(&houses[left], &houses[mid]);
	else
		swap(&houses[left], &houses[right]);

	int pivot = houses[left];
	int k = left;

	for (int i = left + 1; i <= right; i++)
		if (houses[i] < pivot) {
			k++;
			swap(&houses[k], &houses[i]);
		}

	swap(&houses[left], &houses[k]);

	return k;
}

void quick_sort(int left, int right) {
	if (left < right) {
		int pid = get_pivot_idx(left, right);
		quick_sort(left, pid - 1);
		quick_sort(pid + 1, right);
	}
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

	quick_sort(0, N - 1);

	cout << place_wifis(N, C);

	return 0;
}