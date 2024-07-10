#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>

#define INF 998877665544332211

using namespace std;

typedef long long LLT;

class Graph {
private:
	int N, M, K;
	vector<vector<pair<int, int>>> G;

public:
	Graph() {
		cin >> N >> M >> K;
		G = vector<vector<pair<int, int>>>(N + 1);

		for (int i = 0; i < M; i++) {
			int u, v, w;
			cin >> u >> v >> w;
			G[v].push_back({u, w});
		}

		for (int i = 0; i < K; i++) {
			int x;
			cin >> x;
			G[0].push_back({x, 0});
		}
	}

	pair<int, LLT> find() {
		priority_queue<pair<LLT, int>> PQ;
		vector<LLT> dists(N + 1, INF);

		PQ.push({0, 0});
		dists[0] = 0;

		while (!PQ.empty()) {
			LLT d = -PQ.top().first, u = PQ.top().second;
			PQ.pop();

			if (dists[u] < d) continue;

			for (auto [v, w] : G[u])
				if (dists[v] > d + w) {
					dists[v] = d + w;
					PQ.push({-dists[v], v});
				}
		}

		pair<int, LLT> res = {0, 0};
		auto elem_it = max_element(dists.begin(), dists.end());

		res.first = (int) (elem_it - dists.begin());
		res.second = *elem_it;

		return res;
	}
};

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	Graph G;
	pair<int, LLT> res = G.find();

	cout << res.first << '\n';
	cout << res.second;

	return 0;
}