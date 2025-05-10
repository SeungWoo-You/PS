#include <iostream>

#define MAX_N 50

using namespace std;

int pos_nums[MAX_N];
int neg_nums[MAX_N];

void swap(int* a, int* b) {
	int temp = *a;
	*a = *b;
	*b = *a;
}

int partition(int arr[MAX_N], int left, int right) {
	int pivot = arr[left];
	int k = left;

	for (int i = left + 1; i <= right; i++) {
		if (pivot > arr[i]) swap(arr[++k], arr[i]);
	}

	swap(arr[left], arr[k]);

	return k;
}

void quick_sort(int arr[MAX_N], int left, int right) {
	if (left < right) {
		int pivot = partition(arr, left, right);
		quick_sort(arr, left, pivot - 1);
		quick_sort(arr, pivot + 1, right);
	}
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	int N;
	cin >> N;

	int pos_N = 0, neg_N = 0;
	bool has_zero = false;

	for (int i = 0; i < N; i++) {
		int x;
		cin >> x;

		if (x > 0) pos_nums[pos_N++] = x;
		else if (x < 0) neg_nums[neg_N++] = x;
		else has_zero = true;
	}

	quick_sort(pos_nums, 0, pos_N - 1);
	quick_sort(neg_nums, 0, neg_N - 1);

	int total = 0;

	for (int i = pos_N - 1, j = pos_N - 2; i >= 0;) {
		if (j < 0 || pos_nums[j] == 1)
			total += pos_nums[i--];
		else {
			total += pos_nums[i] * pos_nums[j];
			i -= 2, j -= 2;
		}
	}

	for (int i = 0, j = 1; i < neg_N;) {
		if (j == neg_N && !has_zero) total += neg_nums[i++];
		else {
			total += neg_nums[i] * neg_nums[j];
			i += 2, j += 2;
		}
	}

	cout << total;

	return 0;
}