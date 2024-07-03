#include <iostream>
#include <vector>
#include <algorithm>

#define SIZE 65537

using namespace std;

typedef long long LLT;

class SegTree {
private:
	int N, K;
	vector<int> counts;

public:
	vector<int> nums;

	SegTree(int N, int K) {
		this->N = N, this->K = K;
		nums = vector<int>(N);
		counts = vector<int>(4 * SIZE, 0);

		for (int i = 0; i < N; i++) cin >> nums[i];
	}

	void update(int node, int l, int r, int idx, int diff) {
		if (l == r) {
			counts[node] += diff;
			return;
		}

		int mid = (l + r) / 2;
		if (idx <= mid)
			update(node << 1, l, mid, idx, diff);
		else
			update(node << 1 | 1, mid + 1, r, idx, diff);

		counts[node] = counts[node << 1] + counts[node << 1 | 1];
	}

	int find_median(int node, int l, int r, int k) {
		if (l == r) return l;

		int mid = (l + r) / 2;
		if (counts[node << 1] >= k) return find_median(node << 1, l, mid, k);
		else return find_median(node << 1 | 1, mid + 1, r, k - counts[node << 1]);
	}
};

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	int N, K;
	cin >> N >> K;

	SegTree ST(N, K);
	LLT res = 0;

	for (int i = 0; i < (K - 1); i++)
		ST.update(1, 0, SIZE, ST.nums[i], 1);

	for (int l = 0, r = K - 1; r < N; l++, r++) {
		ST.update(1, 0, SIZE, ST.nums[r], 1);
		res += ST.find_median(1, 0, SIZE, (K + 1) / 2);
		ST.update(1, 0, SIZE, ST.nums[l], -1);
	}

	cout << res;

	return 0;
}