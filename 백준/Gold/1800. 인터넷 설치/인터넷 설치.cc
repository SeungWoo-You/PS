#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

#define INF (~0U >> 2)

using namespace std;

class Dijkstra {
private:
	int N, P, K;
	vector<vector<pair<int, int>>> G;

public:
	Dijkstra() {
		cin >> N >> P >> K;
		G.resize(N + 1);

		for (int i = 0; i < P; i++) {
			int u, v, w;
			cin >> u >> v >> w;
			G[u].push_back({v, w});
			G[v].push_back({u, w});
		}
	}

	int find() {
		int start = 0, end = 1000000;
		int res = INF;

		while (start < end) {
			int mid = (start + end) / 2;

			if (run(mid)) res = min(res, mid), end = mid;
			else start = mid + 1;
		}

		return res != INF ? res : -1;
	}

	bool run(int target) {
		vector<int> visited(N + 1, INF);
		priority_queue<pair<int, int>> PQ;
		visited[1] = 0;
		PQ.push({0, 1});

		while (!PQ.empty()) {
			int d = -PQ.top().first;
			int u = PQ.top().second;
			PQ.pop();

			if (visited[u] < d) continue;

			for (int i = 0; i < G[u].size(); i++) {
				int v = G[u][i].first;
				int w = G[u][i].second;
				int next_d = w > target ? d + 1 : d;

				if (visited[v] > next_d) {
					visited[v] = next_d;
					PQ.push({-next_d, v});
				}
			}
		}

		return visited[N] <= K;
	}
};


int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	Dijkstra dijk;

	cout << dijk.find();

	return 0;
}