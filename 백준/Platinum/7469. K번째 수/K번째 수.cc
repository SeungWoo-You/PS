#include <iostream>
#include <vector>
#include <set>
#include <algorithm>

#define INF (~0U >> 1)

using namespace std;

class SegTree {
private:
	int N;
	vector<vector<int>> T;
	vector<int> arr;

	void build(int node, int start, int end) {
		if (start == end) {
			T[node].push_back(arr[start]);
			return;
		}

		int mid = (start + end) / 2;
		build(node << 1, start, mid);
		build(node << 1 | 1, mid + 1, end);

		vector<int>& left = T[node << 1], & right = T[node << 1 | 1];
		auto l = left.begin(), r = right.begin();

		while (l != left.end() || r != right.end()) {
			if (l == left.end())
				T[node].push_back(*r++);
			else if (r == right.end())
				T[node].push_back(*l++);
			else {
				if (*l < *r) T[node].push_back(*l++);
				else T[node].push_back(*r++);
			}
		}
	}

public:
	SegTree(int N) {
		this->N = N;
		T.resize(4 * N);
		arr.resize(N);

		for (int i = 0; i < N; i++)
			cin >> arr[i];

		build(1, 0, N - 1);
	}



	int query(int node, int start, int end,
		int left, int right, int target) {
		if (end < left || right < start)
			return 0;
		else if (left <= start && end <= right)
			return lower_bound(T[node].begin(), T[node].end(), target) - T[node].begin();
		
		int mid = (start + end) / 2;
		
		return query(node << 1, start, mid, left, right, target)
			+ query(node << 1 | 1, mid + 1, end, left, right, target);
	}
};


int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	int N, M;
	cin >> N >> M;
	SegTree ST(N);

	while (M--) {
		int l, r, k;
		cin >> l >> r >> k;

		int answer = -1e9;
		int start = -1e9, end = 1e9;

		while (start <= end) {
			int mid = (start + end) / 2;

			int res = ST.query(1, 0, N - 1, l - 1, r - 1, mid);
			if (res < k) {
				answer = max(answer, mid);
				start = mid + 1;
			}
			else end = mid - 1;
		}

		cout << answer << '\n';
	}

	return 0;
}