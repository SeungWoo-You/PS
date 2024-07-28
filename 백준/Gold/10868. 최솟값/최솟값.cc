#include <iostream>
#include <vector>
#include <algorithm>

#define INF (~0U >> 2)

using namespace std;

class SegTree {
private:
	int N;
	vector<int> T;

public:
	SegTree(int N) {
		this->N = N;
		T.resize(2 * N, INF);

		for (int i = 0; i < N; i++) {
			int x;
			cin >> x;

			update(i, x);
		}
	}

	void update(int i, int val) {
		for (T[i += N] = val; i > 1; i >>= 1)
			T[i >> 1] = min(T[i], T[i ^ 1]);
	}

	int query(int l, int r) {
		int res = INF;

		for (l += N, r += N; l < r; l >>= 1, r >>= 1) {
			if (l % 2) res = min(res, T[l++]);
			if (r % 2)res = min(res, T[--r]);
		}

		return res;
	}
};

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	int N, M;
	cin >> N >> M;
	
	SegTree ST(N);

	while (M--) {
		int a, b;
		cin >> a >> b;

		cout << ST.query(a - 1, b) << '\n';
	}

	return 0;
}