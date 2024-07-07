#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool compare(pair<int, int>& a, pair<int, int>& b) {
	return a.second < b.second;
}

class Game {
private:
	int N;
	vector<int> T;

public:
	vector<pair<int, int>> I;

	Game(int N) {
		this->N = N;
		I.resize(N);
		T.resize(2 * N, 0);

		for (int i = 0; i < N; i++) {
			I[i].first = i;
			cin >> I[i].second;
		}

		sort(I.begin(), I.end(), compare);

		for (int i = 0; i < N; i++) I[i].second = i;
	}

	void update(int i) {
		for (T[i += N] += 1; i > 1; i >>= 1)
			T[i >> 1] = T[i] + T[i ^ 1];
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

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	int N;
	cin >> N;

	vector<pair<int ,int>> res(N);
	Game ST(N);

	for (int i = N - 1; i >= 0; i--) {
		res[i].first = ST.I[i].first;
		ST.update(ST.I[i].first);
		res[i].second = ST.query(0, ST.I[i].first + 1);
	}

	sort(res.begin(), res.end());

	for (auto& [x, y] : res) cout << y << '\n';

	return 0;
}