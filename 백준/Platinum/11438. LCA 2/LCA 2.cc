#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

class LCA {
private:
	int N, K;
	vector<vector<int>> G, table;
	vector<int> depths;

	void build() {
		queue<int> Q;
		Q.push(root);

		while (!Q.empty()) {
			int u = Q.front();
			Q.pop();

			for (int v : G[u])
				if (depths[v] == 0) {
					Q.push(v);

					table[v][0] = u;
					depths[v] = depths[u] + 1;
				}
		}

		init_table();
	}

	void init_table() {
		for (int k = 1; k <= K; k++)
			for (int i = 1; i <= N; i++)
				if (table[i][k - 1] != 0)
					table[i][k] = table[table[i][k - 1]][k - 1];
	}

public:
	int root = 1;

	LCA() {
		cin >> N;

		int temp = N;
		for (int h = 0; temp > 0; temp >>= 1, h++)
			K = h;

		depths = vector<int>(N + 1, 0);
		table = vector<vector<int>>(N + 1, vector<int>(K + 1, 0));
		G = vector<vector<int>>(N + 1);

		for (int i = 0; i < N - 1; i++) {
			int u, v;
			cin >> u >> v;
			G[u].push_back(v);
			G[v].push_back(u);
		}

		depths[root] = 1;

		build();
	}

	int find(int u, int v) {
		if (depths[u] < depths[v]) swap(u, v);

		int diff = depths[u] - depths[v];
		for (int i = 0; diff > 0; diff >>= 1, i++)
			if (diff % 2) u = table[u][i];

		if (u != v) {
			for (int k = K; k >= 0; k--)
				if (table[u][k] != table[v][k])
					u = table[u][k], v = table[v][k];
			u = table[u][0];
		}

		return u;
	}
};

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	LCA lca;

	int M;
	cin >> M;

	while (M--) {
		int u, v;
		cin >> u >> v;
		
		cout << lca.find(u, v) << '\n';
	}

	return 0;
}