#include <iostream>

#define MAX_SIZE 1'000'000

using namespace std;

class Heap {
private:
	long long arr[MAX_SIZE + 1] = {0};
	int hsize = 0;

	void swap(long long* a, long long* b) {
		long long temp = *a;
		*a = *b;
		*b = temp;
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
	void insert(long long val) {
		arr[++hsize] = val;

		int idx = hsize;

		while (idx > 1 && arr[parent(idx)] > arr[idx]) {
			swap(&arr[parent(idx)], &arr[idx]);
			idx = parent(idx);
		}
	}

	long long pop() {
		if (hsize == 1)
			return arr[hsize--];

		long long res = arr[1];
		arr[1] = arr[hsize--];
		heapify(1);

		return res;
	}

	int size() {
		return hsize;
	}
};

Heap heap = Heap{};

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	int T;
	cin >> T;

	while (T--) {
		int N;
		cin >> N;

		for (int i = 0; i < N; i++) {
			long long val;
			cin >> val;

			heap.insert(val);
		}

		long long total = 0;

		while (heap.size()) {
			long long m1 = heap.pop();
			long long m2 = heap.pop();

			total += m1 + m2;
			
			if (heap.size()) heap.insert(m1 + m2);
		}

		cout << total << '\n';
	}

	return 0;
}