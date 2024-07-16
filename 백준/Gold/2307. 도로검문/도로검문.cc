#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

#define INF (~0U >> 2)

using namespace std;

class Graph {
private:
	int N, M;
	vector<vector<pair<int, int>>> G;
	vector<int> dists;
public:
	int root = 1;
	vector<int> parents;

	Graph(int N, int M) {
		this->N = N, this->M = M;
		G.resize(N + 1);
		dists.resize(N + 1, INF);
		parents.resize(N + 1, INF);
		parents[root] = root;

		for (int i = 0; i < M; i++) {
			int u, v, w;
			cin >> u >> v >> w;
			G[u].push_back({v, w});
			G[v].push_back({u, w});
		}
	}

	int find_path(bool block, int blocked_src, int blocked_dst) {
		fill(dists.begin(), dists.end(), INF);
		
		priority_queue<pair<int, int>> PQ;
		PQ.push({0, root});
		dists[root] = 0;

		while (!PQ.empty()) {
			int d = -PQ.top().first;
			int u = PQ.top().second;
			PQ.pop();

			if (d > dists[u]) continue;
			if (u == N) break;

			for (auto [v, w] : G[u]) {
				if (block)
					if ((v == blocked_src && u == blocked_dst) || (u == blocked_src && v == blocked_dst))
						continue;
				if (dists[v] > d + w) {
					if (!block)
						parents[v] = u;
					dists[v] = d + w;
					PQ.push({-dists[v], v});
				}
			}
		}

		return dists[N];
	}
};

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	int N, M;
	cin >> N >> M;

	Graph G(N, M);

	int base = G.find_path(false, 0, 0);
	int answer = 0;

	for (int p = N; p != G.parents[p]; p = G.parents[p]) {
		int blocked_src = p;
		int blocked_dst = G.parents[p];

		int res = G.find_path(true, blocked_src, blocked_dst);

		if (res == INF) {
			cout << -1;
			return 0;
		}

		answer = max(answer, res - base);
	}

	cout << answer;

	return 0;
}