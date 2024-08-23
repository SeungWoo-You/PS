#include <iostream>
#include <vector>
#include <tuple>
#include <queue>
#include <algorithm>

#define INF 998877665544332211
using namespace std;

typedef long long LLT;

class Station {
private:
	int N, M, K = 2500;
	vector<vector<pair<int, int>>> G;
	vector<int> gas_costs;

public:
	Station() {
		cin >> N >> M;
		gas_costs.resize(N + 1, 0);
		G.resize(N + 1);

		for (int i = 1; i <= N; i++)
			cin >> gas_costs[i];
	
		for (int i = 1; i <= M; i++) {
			int u, v, w;
			cin >> u >> v >> w;
			G[u].push_back({v, w});
			G[v].push_back({u, w});
		}
	}

	LLT find() {
		vector<vector<LLT>> costs(N + 1, vector<LLT>(K + 1, INF));
		priority_queue<tuple<LLT, int, int>> PQ;
		costs[1][gas_costs[1]] = 0;
		PQ.push({0, -gas_costs[1], 1});

		while (!PQ.empty()) {
			LLT d = -get<0>(PQ.top());
			int oil = -get<1>(PQ.top());
			int u = get<2>(PQ.top());
			PQ.pop();

			if (d > costs[u][oil]) continue;

			for (auto& [v, w] : G[u]) {
				int temp_oil = min(oil, gas_costs[v]);
				if (costs[v][temp_oil] > d + oil * w) {
					costs[v][temp_oil] = d + oil * w;
					PQ.push({-costs[v][temp_oil], -temp_oil, v});
				}
			}
		}

		return *min_element(costs[N].begin(), costs[N].end());
	}
};

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);
	
	Station S;

	cout << S.find();

	return 0;
}