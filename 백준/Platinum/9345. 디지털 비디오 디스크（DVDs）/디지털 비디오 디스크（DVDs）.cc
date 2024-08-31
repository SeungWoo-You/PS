#include <iostream>
#include <vector>
#include <algorithm>

#define INF (~0U >> 2)

using namespace std;

class SegTree {
private:
	int N;
	vector<pair<int, int>> T;

public:
	SegTree(int N) {
		this->N = N;
		T.resize(2 * N, {INF, 0});

		for (int i = 0; i < N; i++)
			update(i, {i, i});
	}

	void update(int p, pair<int, int> info) {
		T[p += N].first = info.first;
		T[p].second = info.second;

		for (; p > 1; p >>= 1) {
			T[p >> 1].first = min(T[p].first, T[p ^ 1].first);
			T[p >> 1].second = max(T[p].second, T[p ^ 1].second);
		}
	}

	bool query(int l, int r) {
		int l0 = l, r0 = r - 1;
		pair<int, int> res = {INF, 0};

		for (l += N, r += N; l < r; l >>= 1, r >>= 1) {
			if (l % 2) {
				res.first = min(res.first, T[l].first);
				res.second = max(res.second, T[l++].second);
			}
			if (r % 2) {
				res.first = min(res.first, T[--r].first);
				res.second = max(res.second, T[r].second);
			}
		}

		return res.first == l0 && res.second == r0;
	}

	int get_value(int p) {
		return T[p += N].first;
	}
};

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	int T;
	cin >> T;

	while (T--) {
		int N, K;
		cin >> N >> K;

		SegTree ST(N);

		while (K--){
			int cmd, A, B;
			cin >> cmd >> A >> B;
			
			if (cmd == 1)
				cout << (ST.query(A, B + 1) ? "YES" : "NO") << '\n';
			else {
				int x1 = ST.get_value(A), x2 = ST.get_value(B);
				ST.update(A, {x2, x2}), ST.update(B, {x1, x1});
			}
		}
	}

	return 0;
}