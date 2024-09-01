#include <iostream>
#include <vector>

using namespace std;

class SegTree {
private:
	int N;
	vector<int> T, L;

	void apply(int node, int start, int end) {
		if (L[node] != 0) {
			T[node] = (end - start + 1) - T[node];

			if (start != end) {
				L[node << 1] ^= 1;
				L[node << 1 | 1] ^= 1;
			}

			L[node] = 0;
		}
	}

public:
	SegTree(int N) {
		this->N = N;
		T.resize(4 * N, 0), L.resize(4 * N, 0);
	}

	void update(int node, int start, int end, int left, int right) {
		apply(node, start, end);

		if (end < left || right < start)
			return;

		if (left <= start && end <= right) {
			T[node] = (end - start + 1) - T[node];

			if (start != end) {
				L[node << 1] ^= 1;
				L[node << 1 | 1] ^= 1;
			}

			return;
		}

		int mid = (start + end) / 2;
		update(node << 1, start, mid, left, right);
		update(node << 1 | 1, mid + 1, end, left, right);
		T[node] = T[node << 1] + T[node << 1 | 1];

		return;
	}

	int query(int node, int start, int end, int left, int right) {
		apply(node, start, end);
		
		if (end < left || right < start)
			return 0;

		if (left <= start && end <= right)
			return T[node];

		int mid = (start + end) / 2;
		return query(node << 1, start, mid, left, right)
			+ query(node << 1 | 1, mid + 1, end, left, right);
	}
};

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	int N, M;
	cin >> N >> M;

	SegTree ST(N);

	while (M--) {
		int cmd, s, t;
		cin >> cmd >> s >> t;
		
		if (cmd == 0) ST.update(1, 1, N, s, t);
		else cout << ST.query(1, 1, N, s, t) << '\n';
	}

	return 0;
}