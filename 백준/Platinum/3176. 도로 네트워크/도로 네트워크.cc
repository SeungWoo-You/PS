#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>
#include <queue>

#define INF (~0U >> 2)

using namespace std;

class Network {
private:
	int N, K = 0;
	vector<vector<int>> parents;
	vector<vector<pair<int, int>>> lengths;
	vector<unordered_map<int, int>> roads;
	vector<int> depths;

	void build() {
		queue<int> Q;
		Q.push(root);

		while (!Q.empty()) {
			int u = Q.front();
			Q.pop();

			for (auto& [v, w] : roads[u])
				if (depths[v] == 0) {
					lengths[v][0] = {w, w};
					depths[v] = depths[u] + 1;
					parents[v][0] = u;
					Q.push(v);
				}
		}

		init_table();
	}

	void init_table() {
		for (int k = 1; k <= K; k++)
			for (int i = 1; i <= N; i++)
				if (parents[i][k - 1] != 0) {
					parents[i][k] = parents[parents[i][k - 1]][k - 1];
					lengths[i][k].first = min(lengths[i][k - 1].first, lengths[parents[i][k - 1]][k - 1].first);
					lengths[i][k].second = max(lengths[i][k - 1].second, lengths[parents[i][k - 1]][k - 1].second);
				}
	}

public:
	int root = 1;

	Network() {
		cin >> N;

		for (int temp = N; temp > 1; temp >>= 1) K++;

		parents = vector<vector<int>>(N + 1, vector<int>(K + 1, 0));
		lengths = vector<vector<pair<int, int>>>(N + 1, vector<pair<int, int>>(K + 1, {INF, 0}));
		depths = vector<int>(N + 1, 0);
		roads = vector<unordered_map<int, int>>(N + 1);

		for (int i = 0; i < N - 1; i++) {
			int u, v, w;
			cin >> u >> v >> w;
			roads[u][v] = w, roads[v][u] = w;
		}

		depths[root] = 1;
		build();
	}

	pair<int, int> find(int u, int v) {
		pair<int, int> res = {INF, 0};

		if (depths[u] < depths[v]) swap(u, v);

		
		for (int diff = depths[u] - depths[v], i = 0; diff > 0; diff >>= 1, i++)
			if (diff % 2) {
				res.first = min(res.first, lengths[u][i].first);
				res.second = max(res.second, lengths[u][i].second);
				u = parents[u][i];
			}

		if (u != v) {
			for (int k = K;k>=0;k--)
				if (parents[u][k] != parents[v][k]) {
					res.first = min({res.first, lengths[u][k].first, lengths[v][k].first});
					res.second = max({res.second, lengths[u][k].second, lengths[v][k].second});
					u = parents[u][k], v = parents[v][k];
				}
			res.first = min({res.first, lengths[u][0].first, lengths[v][0].first});
			res.second = max({res.second, lengths[u][0].second, lengths[v][0].second});
		}

		return res;
	}
};

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	Network NW;
	
	int K;
	cin >> K;
	while (K--) {
		int u, v;
		cin >> u >> v;

		pair<int, int> res = NW.find(u, v);
		cout << res.first << ' ' << res.second << '\n';
	}

	return 0;
}