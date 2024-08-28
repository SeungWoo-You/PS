#include <iostream>
#include <vector>
#include <algorithm>

#define INF (~0U >> 2)

using namespace std;

class SegTree {
private:
	int N;
	vector<pair<int, int>> T;

	pair<int, int> compare(pair<int, int> p1, pair<int, int> p2) {
		if (p1.first < p2.first) return p1;
		else if (p1.first > p2.first) return p2;
		else {
			if (p1.second < p2.second) return p1;
			else return p2;
		}
	}

public:
	SegTree() {
		cin >> N;
		T.resize(2 * N, {INF, INF});

		for (int i = 0; i < N; i++) {
			int x;
			cin >> x;
			update(i, x);
		}
	}

	void update(int p, int val) {
		pair<int, int> info = {val, p};
		for (T[p += N] = info; p > 1; p >>= 1)
			T[p >> 1] = compare(T[p], T[p ^ 1]);
	}

	int query(int l, int r) {
		pair<int, int> info = {INF, INF};

		for (l += N, r += N; l < r; l >>= 1, r >>= 1) {
			if (l % 2) info = compare(info, T[l++]);
			if (r % 2) info = compare(info, T[--r]);
		}

		return info.second + 1;
	}
};

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	SegTree ST;
	int M;
	cin >> M;

	while (M--) {
		int cmd;
		cin >> cmd;
		
		if (cmd == 1) {
			int p, x;
			cin >> p >> x;
			ST.update(p - 1, x);
		}
		else {
			int l, r;
			cin >> l >> r;
			cout << ST.query(l - 1, r) << '\n';
		}
	}

	return 0;
}