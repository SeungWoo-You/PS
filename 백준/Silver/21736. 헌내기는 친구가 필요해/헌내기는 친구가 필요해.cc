#include <iostream>
#include <vector>
#include <string>
#include <array>
#include <queue>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int N, M;
	cin >> N >> M;
	cin.ignore();

	pair<int, int> init_pos = {0, 0};
	vector<string> campus_map;
	campus_map.resize(N);

	for (int i = 0; i < N; i++) {
		string row;
		getline(cin, row);

		campus_map[i] = row;

		for (int j = 0; j < M; j++) {
			if (campus_map[i][j] == 'I') {
				init_pos.first = i;
				init_pos.second = j;
			}
		}
	}

	int count = 0;
	array<int, 4> Dx = {-1, 1, 0, 0};
	array<int, 4> Dy = {0, 0, -1, 1};
	queue<pair<int, int>> Q;
	vector<vector<bool>> checked;
	checked.resize(N, vector<bool>(M, false));


	Q.push(init_pos);
	checked[init_pos.first][init_pos.second] = true;

	while (!Q.empty()) {
		pair<int, int> pos = Q.front();
		Q.pop();

		int i = pos.first, j = pos.second;

		if (campus_map[i][j] == 'P') count += 1;

		for (int k = 0; k < 4; k++) {
			int x = i + Dx[k], y = j + Dy[k];

			if (0 <= x && x < N && 0 <= y && y < M) {
				if (checked[x][y] || campus_map[x][y] == 'X') continue;

				Q.push({x, y});
				checked[x][y] = true;
			}
		}
	}

	if (count) cout << count;
	else cout << "TT";

	return 0;
}