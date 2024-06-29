#include <iostream>
#include <vector>
#include <unordered_map>
#include <queue>
#include <algorithm>

using namespace std;

class Tree {
private:
	int N, K = 0;
	vector<unordered_map<int, int>> G;
	vector<int> depths;
	vector<vector<int>> parents, dists;
	
	void build() {
		queue<int> Q;
		Q.push(root);

		while (!Q.empty()) {
			int u = Q.front();
			Q.pop();

			for (auto& [v, w] : G[u])
				if (depths[v] == 0) {
					depths[v] = depths[u] + 1;
					parents[v][0] = u;
					dists[v][0] = G[u][v];
					Q.push(v);
				}
		}
	}

	void init_table() {
		for (int k = 1; k <= K; k++)
			for (int i = 1; i <= N; i++)
				if (parents[i][k - 1] != 0) {
					parents[i][k] = parents[parents[i][k - 1]][k - 1];
					dists[i][k] = dists[i][k - 1] + dists[parents[i][k - 1]][k - 1];
				}
	}

public:
	int root = 1;

	Tree() {
		cin >> N;

		for (int temp = N; temp > 1; temp >>= 1)
			K++;

		parents = vector<vector<int>>(N + 1, vector<int>(K + 1, 0));
		dists = vector<vector<int>>(N + 1, vector<int>(K + 1, 0));
		depths = vector<int>(N + 1, 0);
		G = vector<unordered_map<int, int>>(N + 1);
		
		for (int i = 0; i < N - 1; i++) {
			int u, v, w;
			cin >> u >> v >> w;
			G[u][v] = w;
			G[v][u] = w;
		}

		depths[root] = 1;
		build();
		init_table();
	}

	int find(int u, int v) {
		int res = 0;

		if (depths[u] < depths[v]) swap(u, v);

		int diff = depths[u] - depths[v];
		
		for (int i = 0; diff > 0; diff >>= 1, i++)
			if (diff % 2) {
				int p = parents[u][i];
				res += dists[u][i];
				u = parents[u][i];
			}

		if (u != v) {
			for (int k = K; k >= 0; k--)
				if (parents[u][k] != parents[v][k]) {
					res += dists[u][k] + dists[v][k];
					u = parents[u][k], v = parents[v][k];
				}
			res += dists[u][0] + dists[v][0];
		}

		return res;
	}
};

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	Tree T;

	int M;
	cin >> M;

	while (M--) {
		int u, v;
		cin >> u >> v;

		cout << T.find(u, v) << '\n';
	}

	return 0;
}