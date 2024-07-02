#include <iostream>
#include <vector>
#include <array>
#include <queue>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	int M, N;
	cin >> M >> N;

	vector<vector<int>> slope_map(M, vector<int>(N)), DP(M, vector<int>(N, 0));
	for (int i = 0; i < M; i++)
		for (int j = 0; j < N; j++)
			cin >> slope_map[i][j];

	priority_queue<array<int, 3>> PQ;
	PQ.push({slope_map[0][0], 0, 0});

	array<int, 4> Dx = {0, 0, -1, 1};
	array<int, 4> Dy = {-1, 1, 0, 0};
	DP[0][0] = 1;

	while (!PQ.empty()) {
		auto [_, i, j] = PQ.top();
		PQ.pop();

		for (int d = 0; d < 4; d++) {
			int dx = Dx[d], dy = Dy[d];
			int x = i + dx, y = j + dy;

			if (0 <= x && x < M && 0 <= y && y < N)
				if (slope_map[i][j] > slope_map[x][y]) {
					if (DP[x][y] == 0)
						PQ.push({slope_map[x][y], x, y});
					DP[x][y] += DP[i][j];
				}
		}
	}

	cout << DP[M - 1][N - 1];

	return 0;
}