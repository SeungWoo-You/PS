#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	int N;
	cin >> N;

	vector<vector<int>> G(N + 1);
	for (int i = 0; i < N - 1; i++) {
		int u, v;
		cin >> u >> v;
		G[u].push_back(v);
		G[v].push_back(u);
	}

	vector<int> depths(N + 1, 0), parents(N + 1, 0);
	vector<bool> checked(N + 1, false);
	checked[1] = true;
	
	queue<int> Q;
	Q.push(1);

	while (!Q.empty()) {
		int u = Q.front();
		Q.pop();

		for (int v : G[u]) {
			if (!checked[v]) {
				depths[v] = depths[u] + 1;
				checked[v] = true;
				parents[v] = u;
				Q.push(v);
			}
		}
	}

	int M;
	cin >> M;

	while (M--) {
		int u, v;
		cin >> u >> v;

		if (depths[u] > depths[v]) swap(u, v);

		while (depths[u] != depths[v]) v = parents[v];

		while (u != v)
			u = parents[u], v = parents[v];

		cout << u << '\n';
	}

	return 0;
}