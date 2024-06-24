#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void update(vector<int>* T, int N, int i, int val) {
	for ((*T)[i += N] = val; i > 1; i >>= 1)
		(*T)[i >> 1] = max((*T)[i], (*T)[i ^ 1]);

	return;
}

int query(vector<int>* T, int N, int l, int r) {
	int res = 0;
	
	for (l += N, r += N; l < r; l >>= 1, r >>= 1) {
		if (l % 2) res = max(res, (*T)[l++]);
		if (r % 2) res = max(res, (*T)[--r]);
	}
	
	return res;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int N, M;
	cin >> N >> M;

	vector<int> lights(2 * N, 0);

	for (int i = 0; i < N; i++) {
		int x;
		cin >> x;

		update(&lights, N, i, x);
	}

	for (int i = M - 1; i < N - M + 1; i++)
		cout << query(&lights, N, i - M + 1, i + M) << ' ';

	return 0;
}