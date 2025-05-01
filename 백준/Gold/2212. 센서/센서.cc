#include <iostream>

#define MAX_N 10'000

using namespace std;

int negs[MAX_N] = {0};
int poss[MAX_N] = {0};
int temps[MAX_N];

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

class Heap {
	int arr[1001] = {0};
	int total = 0;
	int hsize = 0;

	void swap(int* x, int* y) {
		int temp = *x;
		*x = *y;
		*y = temp;
	}

	int parent(int i) {
		return i >> 1;
	}

	int left_child(int i) {
		return i << 1;
	}

	int right_child(int i) {
		return i << 1 | 1;
	}

	void heapify(int idx) {
		int s = idx;
		int left = left_child(idx);
		int right = right_child(idx);

		if (left <= hsize && arr[left] < arr[s]) s = left;
		if (right <= hsize && arr[right] < arr[s]) s = right;

		if (s != idx) {
			swap(&arr[s], &arr[idx]);
			heapify(s);
		}
	}

public:
	void push(int K, int val) {
		arr[++hsize] = val;
		total += val;

		int idx = hsize;

		while (idx > 1 && arr[parent(idx)] > arr[idx]) {
			swap(&arr[parent(idx)], &arr[idx]);
			idx = parent(idx);
		}

		if (hsize > K - 1)
			pop();
	}

	int pop() {
		if (hsize == 1) {
			total -= arr[1];

			return arr[hsize--];
		}

		int res = arr[1];
		total -= res;
		arr[1] = arr[hsize--];
		heapify(1);

		return res;
	}

	int size() {
		return hsize;
	}

	int get_sum() {
		return total;
	}
};

Heap heap = Heap {};

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

	int total = 0;
	int diff;

	for (int i = 0; i < neg_N - 1; i++) {
		diff = negs[i + 1] - negs[i];
		total += diff;
		heap.push(K, diff);
	}

	if (pos_N > 0 && neg_N > 0) {
		diff = poss[0] + negs[0];
		total += diff;
		heap.push(K, diff);
	}

	for (int i = 0; i < pos_N - 1; i++) {
		diff = poss[i + 1] - poss[i];
		total += diff;
		heap.push(K, diff);
	}

	cout << total - heap.get_sum();

	return 0;
}