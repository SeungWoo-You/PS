#include <iostream>
#include <vector>
#include <queue>

#define INF (~0U >> 2)

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	int T;
	cin >> T;

	while (T--) {
		int N, D, C;
		cin >> N >> D >> C;
		vector<vector<pair<int, int>>> G(N + 1);
		
		for (int i = 0; i < D; i++) {
			int u, v, w;
			cin >> u >> v >> w;
			G[v].push_back({u, w});
		}

		vector<int> dists(N + 1, INF);
		priority_queue<pair<int, int>> PQ;
		PQ.push({0, C});
		dists[C] = 0;

		while (!PQ.empty()) {
			int d = -PQ.top().first;
			int u = PQ.top().second;
			PQ.pop();

			if (dists[u] < d) continue;

			for (auto [v, w] : G[u])
				if (dists[v] > d + w) {
					dists[v] = d + w;
					PQ.push({-dists[v], v});
				}
		}

		int sec = 0, cnt = 0;
		for (int i = 1; i <= N; i++) {
			if (dists[i] == INF) continue;
			sec = max(sec, dists[i]);
			cnt++;
		}

		cout << cnt << ' ' << sec << '\n';
	}

	return 0;
}