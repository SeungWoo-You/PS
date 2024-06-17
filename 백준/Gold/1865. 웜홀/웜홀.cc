#include <iostream>
#include <vector>
#include <unordered_map>

#define INF (~0U >> 2)

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int TC;
	cin >> TC;

	while (TC--) {
		int N, M, W;
		cin >> N >> M >> W;

		unordered_map<int, vector<pair<int, int>>> graph;
		for (int i = 0; i < M; i++) {
			int S, E, T;
			cin >> S >> E >> T;

			graph[S].push_back({E, T});
			graph[E].push_back({S, T});
		}

		for (int i = 0; i < W; i++) {
			int S, E, T;
			cin >> S >> E >> T;

			graph[S].push_back({E, -T});
		}

		string answer = "NO";
		vector<int> dists(N + 1, INF);
		dists[1] = 0;

		for (int i = 1; i <= N; i++) {
			for (int u = 1; u <= N; u++) {
				for (int j = 0; j < graph[u].size(); j++) {
					int v = graph[u][j].first, w = graph[u][j].second;
					
					if (dists[v] > dists[u] + w) {
						dists[v] = dists[u] + w;
						
						if (i == N) answer = "YES";
					}
				}
			}
		}

		cout << answer << '\n';
	}

	return 0;
}