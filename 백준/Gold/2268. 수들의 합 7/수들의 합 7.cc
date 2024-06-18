#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

typedef long long LLT;

void update(vector<LLT>* T, int N, int i, LLT val) {
	for ((*T)[i += N] = val; i > 1; i >>= 1)
		(*T)[i >> 1] = (*T)[i] + (*T)[i ^ 1];

	return;
}

LLT query(vector<LLT>* T, int N, int l, int r) {
	LLT res = 0;

	for (l += N, r += N; l < r; l >>= 1, r >>= 1) {
		if (l % 2) res += (*T)[l++];
		if (r % 2) res += (*T)[--r];
	}

	return res;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int N, M;
	cin >> N >> M;

	vector<LLT> T(2 * N, 0);

	while (M--) {
		int cmd, x, y;
		cin >> cmd >> x >> y;

		if (cmd == 0) {
			int i = min(x, y), j = max(x, y);
			cout << query(&T, N, i - 1, j) << '\n';
		}
		else if (cmd == 1) update(&T, N, x - 1, (LLT) y);
	}

	return 0;
}