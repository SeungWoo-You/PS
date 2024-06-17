#include <iostream>
#include <vector>

using namespace std;

void update(vector<vector<int>>* T, int N, int x, int y, int val) {
	int i = x + N, j = y + N;
	for ((*T)[i][j] = val; j > 1; j >>= 1)
		(*T)[i][j >> 1] = (*T)[i][j] + (*T)[i][j ^ 1];

	for (; i > 1; i >>= 1) {
		j = y + N;
		(*T)[i >> 1][j] = (*T)[i][j] + (*T)[i ^ 1][j];

		for (; j > 1; j >>= 1)
			(*T)[i >> 1][j >> 1] = (*T)[i >> 1][j] + (*T)[i >> 1][j ^ 1];
	}

	return;
}

int query(vector<vector<int>>* T, int N, int x1, int y1, int x2, int y2) {
	int res = 0;
	
	for (x1 += N, x2 += N; x1 < x2; x1 >>= 1, x2 >>= 1) {
		if (x1 % 2) {
			for (int j1 = y1 + N, j2 = y2 + N; j1 < j2; j1 >>= 1, j2 >>= 1) {
				if (j1 % 2) res += (*T)[x1][j1++];
				if (j2 % 2) res += (*T)[x1][--j2];
			}
			x1++;
		}
		if (x2 % 2) {
			--x2;
			for (int j1 = y1 + N, j2 = y2 + N; j1 < j2; j1 >>= 1, j2 >>= 1) {
				if (j1 % 2) res += (*T)[x2][j1++];
				if (j2 % 2) res += (*T)[x2][--j2];
			}
		}
	}

	return res;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int N, M;
	cin >> N >> M;

	vector<vector<int>> T(2 * N, vector<int>(2 * N, 0));
	for (int i = 0; i < N; i++)
		for (int j = 0; j < N; j++) {
			int x;
			cin >> x;

			update(&T, N, i, j, x);
		}

	while (M--) {
		int x1, y1, x2, y2;
		cin >> x1 >> y1 >> x2 >> y2;
		cout << query(&T, N, x1 - 1, y1 - 1, x2, y2) << '\n';
	}

	return 0;
}