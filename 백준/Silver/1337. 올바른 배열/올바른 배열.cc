#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>

#define MAX 50

int arr[MAX];

void swap(int* a, int* b) {
	int temp = *a;
	*a = *b;
	*b = temp;
}

int partition(int left, int right) {
	int pivot = arr[left];
	int k = left;

	for (int i = left + 1; i <= right; i++) {
		if (arr[i] < pivot)
			swap(&arr[++k], &arr[i]);
	}

	swap(&arr[k], &arr[left]);

	return k;
}

void quick_sort(int left, int right) {
	if (left < right) {
		int p = partition(left, right);
		quick_sort(left, p - 1);
		quick_sort(p + 1, right);
	}
}

int main() {
	int N;

	scanf("%d", &N);

	for (int i = 0; i < N; i++)
		scanf("%d", &arr[i]);

	quick_sort(0, N - 1);

	int result = 4, conts = 1;
	int left = 0;
	int prev = arr[left];

	for (int i = 1; i < N; i++) {
		if (arr[i] - arr[left] > 4) {
			result = 5 - conts < result ? 5 - conts : result;
			left = i;
			conts = 1;
		}
		else if (arr[i] - arr[left] == 4) {
			conts++;
			result = 5 - conts < result ? 5 - conts : result;
			left++;
			conts--;
		}
		else
			conts++;

		prev = arr[i];
	}

	result = 5 - conts < result ? 5 - conts : result;

	printf("%d", result);

	return 0;
}