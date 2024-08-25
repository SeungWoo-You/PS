#include <iostream>
#include <vector>

using namespace std;

class SegTree {
private:
	int N;
	vector<int> T;

public:
	SegTree(int N) {
		this->N = N;
		T.resize(2 * N, 0);
	}

	void update(int p, int val) {
		for (T[p += N] = val; p > 1; p >>= 1)
			T[p >> 1] = T[p] + T[p ^ 1];
	}

	int query(int l, int r) {
		int res = 0;

		for (l += N, r += N; l < r; l >>= 1, r >>= 1) {
			if (l % 2) res += T[l++];
			if (r % 2) res += T[--r];
		}

		return res;
	}
};

class SegTree2D {
private:
	int N;
	vector<SegTree> T;

public:
	SegTree2D(int N) {
		this->N = N;
		T.resize(2 * N, SegTree(N));

		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				int val;
				cin >> val;
				update(i, j, val);
			}
		}
	}

	void update(int x, int y, int val) {
		for (T[x += N].update(y, val); x > 1; x >>= 1)
			T[x >> 1].update(y, T[x].query(y, y + 1) + T[x ^ 1].query(y, y + 1));
	}

	int query(int x1, int y1, int x2, int y2) {
		int res = 0;

		for (x1 += N, x2 += N; x1 < x2; x1 >>= 1, x2 >>= 1) {
			if (x1 % 2) res += T[x1++].query(y1, y2);
			if (x2 % 2) res += T[--x2].query(y1, y2);
		}

		return res;
	}
};


int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	int N, M;
	cin >> N >> M;

	SegTree2D ST(N);

	while (M--) {
		int cmd;
		cin >> cmd;

		if (cmd == 0) {
			int x, y, val;
			cin >> x >> y >> val;

			ST.update(x - 1, y - 1, val);
		}

		if (cmd == 1) {
			int x1, y1, x2, y2;
			cin >> x1 >> y1 >> x2 >> y2;

			cout << ST.query(x1 - 1, y1 - 1, x2, y2) << '\n';
		}
	}

	return 0;
}