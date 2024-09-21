#include <iostream>
#include <vector>
#include <queue>
#include <tuple>

#define INF (~0U >> 2)

using namespace std;

class Cave {
private:
	int N;
	int sx = 0, sy = 0;
	vector<vector<int>> G;

public:
	Cave(int N) {
		this->N = N;
		G.resize(N, vector<int>(N));

		for (int i = 0; i < N; i++)
			for (int j = 0; j < N; j++)
				cin >> G[i][j];
	}

	int escape() {
		vector<vector<int>> dists(N, vector<int>(N, INF));
		priority_queue<tuple<int, int, int>> PQ;
		dists[sx][sy] = G[sx][sy];
		PQ.push({-dists[sx][sy], sx, sy});

		int Dx[4] = {0, 0, -1, 1},
			Dy[4] = {-1, 1, 0, 0};

		while (!PQ.empty()) {
			int d = -get<0>(PQ.top()),
				i = get<1>(PQ.top()),
				j = get<2>(PQ.top());
			PQ.pop();

			if (dists[i][j] < d) continue;
			if (i == N - 1 && j == N - 1)
				return dists[i][j];

			for (int k = 0; k < 4; k++) {
				int x = i + Dx[k], y = j + Dy[k];

				if (0 <= x && x < N && 0 <= y && y < N)
					if (dists[x][y] > d + G[x][y]) {
						dists[x][y] = d + G[x][y];
						PQ.push({-dists[x][y], x, y});
					}
			}
		}

		return INF;
	}
};


int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	int N, idx = 1;
	cin >> N;

	while (N != 0) {
		Cave cave(N);

		cout << "Problem " << idx++ << ": "
			<< cave.escape() << '\n';

		cin >> N;
	}

	return 0;
}