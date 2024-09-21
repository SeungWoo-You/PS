#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

#define INF (~0U >> 2)

using namespace std;

typedef vector<vector<pair<int, int>>> Graph;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	int N, M, X;
	cin >> N >> M >> X;

	Graph G(N + 1), RG(N + 1);
	for (int i = 0; i < M; i++) {
		int u, v, w;
		cin >> u >> v >> w;
		G[u].push_back({v, w});
		RG[v].push_back({u, w});
	}

	vector<int> dists(N + 1, INF);
	priority_queue<pair<int, int>> PQ;
	dists[X] = 0;
	PQ.push({0, X});

	while (!PQ.empty()) {
		int d = -PQ.top().first,
			u = PQ.top().second;
		PQ.pop();

		if (dists[u] < d) continue;

		for (auto& [v, w] : G[u])
			if (dists[v] > d + w) {
				dists[v] = d + w;
				PQ.push({-dists[v], v});
			}
	}

	vector<int> rdists(N + 1, INF);
	rdists[X] = 0;
	PQ.push({0, X});

	while (!PQ.empty()) {
		int d = -PQ.top().first,
			u = PQ.top().second;
		PQ.pop();

		if (rdists[u] < d) continue;

		for (auto& [v, w] : RG[u])
			if (rdists[v] > d + w) {
				rdists[v] = d + w;
				PQ.push({-rdists[v], v});
			}
	}

	int res = 0;
	for (int i = 1; i <= N; i++) {
		res = max(res, dists[i] + rdists[i]);
	}

	cout << res;

	return 0;
}