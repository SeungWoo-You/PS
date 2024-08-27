#include <iostream>
#include <vector>
#include <queue>
#include <string>
#include <tuple>
#include <algorithm>

#define INF (~0U >> 2)

using namespace std;

class Layser {
private:
	int W, H;
	vector<string> maze;
	pair<int, int> S = {-1, -1}, D = {-1, -1};

public:
	Layser() {
		cin >> W >> H;
		maze.resize(H, "");

		for (int i = 0; i < H; i++)
			cin >> maze[i];

		bool checked_S = false, checked_D = false;
		for (int i = 0; i < H; i++) {
			for (int j = 0; j < W; j++)
				if (maze[i][j] == 'C') {
					if (checked_S == false) {
						checked_S = true;
						S.first = i, S.second = j;
					}
					else {
						checked_D = true;
						D.first = i, D.second = j;
					}
					
				}
			if (checked_S == true && checked_D == true) break;
		}
	}

	int connect() {
		vector<vector<vector<int>>> mirror(H, vector<vector<int>>(W, vector<int>(4, INF)));
		vector<vector<vector<bool>>> visited(H, vector<vector<bool>>(W, vector<bool>(4, false)));
		queue<tuple<int, int, int, int>> Q;
		for (int k = 0; k < 4; k++) {
			mirror[S.first][S.second][k] = 0;
			visited[S.first][S.second][k] = true;
		}
		Q.push({0, -1, S.first, S.second});

		int Dx[4] = {0, 0, -1, 1};
		int Dy[4] = {-1, 1, 0, 0};

		while (!Q.empty()) {
			int cnt = get<0>(Q.front());
			int direction = get<1>(Q.front());
			int i = get<2>(Q.front());
			int j = get<3>(Q.front());
			Q.pop();

			for (int d = 0; d < 4; d++) {
				int dx = Dx[d], dy = Dy[d];
				int x = i + dx, y = j + dy;

				if (0 <= x && x < H && 0 <= y && y < W && maze[x][y] != '*') {
					if (direction == -1) {
						if (mirror[x][y][d] > cnt) {
							visited[x][y][d] = true;
							mirror[x][y][d] = cnt;
							Q.push({cnt, d, x, y});
						}
					}
					else {
						int next_cnt = cnt;
						if (direction != d) next_cnt++;
						if (mirror[x][y][d] > next_cnt) {
							visited[x][y][d] = true;
							mirror[x][y][d] = next_cnt;
							Q.push({next_cnt, d, x, y});
						}
					}
				}
			}
		}

		int res = INF;
		for (int k = 0; k < 4; k++)
			if (visited[D.first][D.second][k])
				res = min(res, mirror[D.first][D.second][k]);

		return res;
	}
};

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	Layser layser;

	cout << layser.connect();

	return 0;
}