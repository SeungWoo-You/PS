#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>

#define MAX_N 15'000

int arr[MAX_N + 1];

void swap(int* a, int* b) {
	int temp = *a;
	*a = *b;
	*b = temp;
}

int partition(int left, int right) {
	int target = arr[left];
	int k = left;

	for (int i = left + 1; i <= right; i++) {
		if (target > arr[i]) swap(&arr[++k], &arr[i]);
	}

	swap(&arr[left], &arr[k]);

	return k;
}

void quick_sort(int left, int right) {
	if (left < right) {
		int k = partition(left, right);
		quick_sort(left, k - 1);
		quick_sort(k + 1, right);
	}
}


int main() {
	int M, N;

	scanf("%d %d", &N, &M);

	for (int i = 0; i < N; i++)
		scanf("%d", &arr[i]);

	quick_sort(0, N - 1);

	int left = 0, right = N - 1;
	int count = 0;

	while (left < right) {
		int sum = arr[left] + arr[right];

		if (sum == M) {
			count++;
			left++;
		}
		else if (sum < M) left++;
		else right--;
	}

	printf("%d", count);

	return 0;
}