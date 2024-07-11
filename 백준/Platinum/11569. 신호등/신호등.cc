#include <iostream>
#include <queue>
#include <vector>
#include <climits>
#include <algorithm>
#include <tuple>

using namespace std;

typedef long long LLT;

class Traffic {
private:
	int N, M, S, D;
	vector<vector<pair<int, LLT>>> roads;
	vector<int> delays;
public:
	Traffic() {
		cin >> N >> M >> S >> D;
		roads.resize(N + 1);
		delays.resize(N + 1, 0);

		for (int i = 0; i < M; i++) {
			int u, v;
			LLT w;
			cin >> u >> v >> w;
			roads[u].push_back({v, w});
			roads[v].push_back({u, w});
		}

		for (int i = 1; i <= N; i++) {
			cin >> delays[i];
			sort(roads[i].begin(), roads[i].end());
		}
	}

	LLT solve() {
		priority_queue<tuple<LLT, int, int>> PQ;
		vector<LLT> dists(N + 1, LLONG_MAX);
		dists[S] = 0;

		for (auto [v, w] : roads[S]) {
			PQ.push({-w, S, v});
			dists[v] = w;
		}

		while (!PQ.empty()) {
			LLT d = -get<0>(PQ.top());
			int from = get<1>(PQ.top()), u = get<2>(PQ.top());
			PQ.pop();

			if (u == D) return dists[u];

			int K = (int) roads[u].size();
			LLT T = d;
			int P = delays[u];
			LLT cycle_count = T / P;
			LLT now_on_idx = cycle_count % K;

			int from_idx = 0;
			for (; from_idx < K; from_idx++)
				if (roads[u][from_idx].first == from) break;

			if (from_idx != now_on_idx) {
				LLT wait_count = (from_idx + K - now_on_idx) % K;
				T = (cycle_count + wait_count) * P;
			}

			for (int i = 0; i < K; i++) {
				int v = roads[u][i].first;
				LLT w = roads[u][i].second;

				if (dists[v] > T + w) {
					dists[v] = T + w;
					PQ.push({-dists[v], u, v});
				}
			}
		}

		if (dists[D] != LLONG_MAX)
			return dists[D];

		return -1;
	}
};

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	int T;
	cin >> T;

	while (T--) {
		Traffic TF;
		cout << TF.solve() << '\n';
	}

	return 0;
}