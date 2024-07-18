#include <iostream>
#include <vector>
#include <queue>
#include <climits>
#include <tuple>
#include <algorithm>

using namespace std;

typedef long long LLT;

class Road {
private:
	int N, M, K;
	vector<vector<pair<int, int>>> G;

public:
	int root = 1;

	Road() {
		cin >> N >> M >> K;
		G.resize(N + 1);

		for (int i = 0; i < M; i++) {
			int u, v, w;
			cin >> u >> v >> w;
			G[u].push_back({v, w});
			G[v].push_back({u, w});
		}
	}

	LLT pave() {
		priority_queue<tuple<LLT, int, int>> PQ;
		vector<vector<LLT>> dists(N + 1, vector<LLT>(K + 1, LLONG_MAX));
		
		PQ.push({0, root, 0});
		dists[root][0] = 0;

		while (!PQ.empty()) {
			LLT d = -get<0>(PQ.top());
			int u = get<1>(PQ.top()), k = get<2>(PQ.top());
			PQ.pop();

			if (d > dists[u][k]) continue;

			for (auto [v, w] : G[u]) {
				if (dists[v][k] > d + w) {
					dists[v][k] = d + w;
					PQ.push({-dists[v][k], v, k});
				}
				if (k < K && dists[v][k + 1] > d) {
					dists[v][k + 1] = d;
					PQ.push({-dists[v][k + 1], v, k + 1});
				}
			}
		}

		return *min_element(dists[N].begin(), dists[N].end());
	}

};

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	Road R;
	cout << R.pave();

	return 0;
}