#include <iostream>
#include <vector>
#include <array>
#include <queue>
#include <algorithm>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int M, N, H;
	cin >> M >> N >> H;

	vector<vector<vector<int>>> tomatos, checked;
	tomatos.resize(H, vector<vector<int>>(N, vector<int>(M)));
	checked.resize(H, vector<vector<int>>(N, vector<int>(M, -1)));
	queue<array<int, 3>> Q;

	for (int i = 0; i < H; i++)
		for (int j = 0; j < N; j++)
			for (int k = 0; k < M; k++) {
				int t;
				cin >> t;

				tomatos[i][j][k] = t;

				if (t == 1) {
					Q.push({i, j, k});
					checked[i][j][k] = 0;
				}
			}

	array<int, 6> Dh = {1, -1, 0, 0, 0, 0}, Dn = {0, 0, 1, -1, 0, 0}, Dm = {0, 0, 0, 0, 1, -1};

	while (!Q.empty()) {
		array<int, 3>& pos = Q.front();
		int i = pos[0], j = pos[1], k = pos[2];

		for (int d = 0; d < 6; d++) {
			int dh = Dh[d], dn = Dn[d], dm = Dm[d];
			int h = i + dh, n = j + dn, m = k + dm;

			if (0 <= h && h < H && 0 <= n && n < N && 0 <= m && m < M)
				if (checked[h][n][m] == -1 && tomatos[h][n][m] == 0) {
					tomatos[h][n][m] = 1;
					checked[h][n][m] = checked[i][j][k] + 1;
					Q.push({h, n, m});
				}
		}

		Q.pop();
	}

	int result = 0;

	for (int i = 0; i < H; i++)
		for (int j = 0; j < N; j++) {
			result = max(result, *max_element(checked[i][j].begin(), checked[i][j].end()));

			if (count(tomatos[i][j].begin(), tomatos[i][j].end(), 0)) {
				cout << -1;

				return 0;
			}
		}

	cout << result;

	return 0;
}