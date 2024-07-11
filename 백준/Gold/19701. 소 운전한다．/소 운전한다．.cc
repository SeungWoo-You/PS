#include <iostream>
#include <vector>
#include <climits>
#include <tuple>
#include <queue>
#include <algorithm>

#define PASS 0
#define EAT 1

using namespace std;

typedef long long LLT;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	int V, E;
	cin >> V >> E;

	vector<vector<tuple<int, int, int>>> roads(V + 1);
	for (int i = 0; i < E; i++) {
		int x, y, t, k;
		cin >> x >> y >> t >> k;
		roads[x].push_back({y, t, k});
		roads[y].push_back({x, t, k});
	}

	vector<vector<LLT>> costs(V + 1, vector<LLT>(2, LLONG_MAX));
	priority_queue<tuple<LLT, int, int>> PQ;

	costs[1][PASS] = 0;
	PQ.push({0, PASS, 1});

	while (!PQ.empty()) {
		LLT C = -get<0>(PQ.top());
		int trial = get<1>(PQ.top());
		int u = get<2>(PQ.top());
		PQ.pop();

		if (costs[u][trial] < C) continue;

		for (int i = 0; i < roads[u].size(); i++) {
			int v = get<0>(roads[u][i]);
			int t = get<1>(roads[u][i]);
			int k = get<2>(roads[u][i]);

			if (trial == PASS) {
				if (costs[v][EAT] > C + t - k) {
					costs[v][EAT] = C + t - k;
					PQ.push({-costs[v][EAT], EAT, v});
				}
			}

			if (costs[v][trial] > C + t) {
				costs[v][trial] = C + t;
				PQ.push({-costs[v][trial], trial, v});
			}
		}
	}

	for (int i = 2; i <= V; i++)
		cout << min(costs[i][PASS], costs[i][EAT]) << '\n';

	return 0;
}