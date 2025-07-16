#include <iostream>

#define MAX_N 1'000'000
#define MAX_POS 11

using namespace std;

class MaxPlayerHeap {
private:
	int heap[MAX_N + 1] = {0};
	int hsize = 0;

	int parent(int i) {
		return i >> 1;
	}

	int left(int i) {
		return i << 1;
	}

	int right(int i) {
		return i << 1 | 1;
	}

	void swap_nodes(int i, int j) {
		int temp = heap[i];
		heap[i] = heap[j];
		heap[j] = temp;
	}

	bool compare(int val1, int val2) {
		return val1 < val2;
	}

	void up_heap(int i) {
		while (i > 1 && compare(heap[parent(i)], heap[i])) {
			swap_nodes(parent(i), i);
			i = parent(i);
		}
	}

	void down_heap(int i) {
		while (true) {
			int l = left(i), r = right(i), largest = i;

			if (l <= hsize && compare(heap[largest], heap[l])) largest = l;
			if (r <= hsize && compare(heap[largest], heap[r])) largest = r;
			if (largest == i) break;

			swap_nodes(largest, i);
			i = largest;
		}
	}

public:
	void insert(int val) {
		heap[++hsize] = val;
		up_heap(hsize);
	}

	void update_top() {
		if (hsize == 0) return;

		heap[1]--;

		if (heap[1] == 0) erase_top();
		else down_heap(1);
	}

	void erase_top() {
		if (hsize == 0) return;

		swap_nodes(1, hsize--);
		down_heap(1);
	}

	int get_top() {
		return heap[1];
	}
};

MaxPlayerHeap heaps[MAX_POS];

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	int N, K;
	cin >> N >> K;

	for (int i = 0; i < N; i++) {
		int pos, val;
		cin >> pos >> val;

		heaps[pos - 1].insert(val);
	}

	for (int i = 0; i < K; i++)
		for (int p = 0; p < MAX_POS; p++)
			heaps[p].update_top();

	long long total = 0;

	for (int p = 0; p < MAX_POS; p++)
		total += heaps[p].get_top();

	cout << total;

	return 0;
}