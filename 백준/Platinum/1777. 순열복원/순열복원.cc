#include <iostream>
#include <vector>

using namespace std;

void update(vector<int>* T, int N, int i, int val) {
	for ((*T)[i += N] = val; i > 1; i >>= 1)
		(*T)[i >> 1] = (*T)[i] + (*T)[i ^ 1];

	return;
}

int query(vector<int>* T, int N, int l, int r) {
	int res = 0;

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

	int N;
	cin >> N;

	vector<int> inv_seq(N, 0), spaces(2 * N, 0), answer(N, 0);
	for (int i = 0; i < N; i++) {
		cin >> inv_seq[i];
		update(&spaces, N, i, 1);
	}

	for (int x = N - 1; x >= 0; x--) {
		int start = 0, end = N;

		while (start <= end) {
			int mid = (start + end) / 2;
			int total = query(&spaces, N, mid, N);

			if (total > inv_seq[x])
				start = mid + 1;
			else
				end = mid - 1;
		}

		answer[start - 1] = x + 1;
		update(&spaces, N, start - 1, 0);
	}

	for (int x : answer) cout << x << ' ';

	return 0;
}