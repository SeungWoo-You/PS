#include <iostream>
#include <vector>
#include <queue>
#include <tuple>
#include <algorithm>

#define INF (~0U >> 2)

using namespace std;

bool compare(tuple<int, int, int> A, tuple<int, int, int> B) {
	return get<2>(A) < get<2>(B);
}

class KCM {
private:
	int N, M, K;
	vector<vector<tuple<int, int, int>>> G;

public:
	KCM() {
		cin >> N >> M >> K;
		G.resize(N + 1);

		for (int i = 0; i < K; i++) {
			int u, v, c, d;
			cin >> u >> v >> c >> d;
			G[u].push_back({v, c, d});
		}

		for (int i = 1; i <= N; i++)
			sort(G[i].begin(), G[i].end(), compare);
	}

	int find() {
		vector<vector<int>> costs(N + 1, vector<int>(M + 1, INF));
		priority_queue<tuple<int, int, int>> PQ;
		costs[1][0] = 0;
		PQ.push({0, 0, 1});

		while (!PQ.empty()) {
			int d = -get<0>(PQ.top());
			int c = get<1>(PQ.top());
			int u = get<2>(PQ.top());
			PQ.pop();

			if (d > costs[u][c]) continue;

			for (auto& [v, cw, dw] : G[u]) {
				int next_c = c + cw, next_d = d + dw;

				if (next_c > M) continue;

				if (costs[v][next_c] > next_d) {
					for (int i = next_c + 1; i <= M; i++) {
						if (costs[v][i] < next_d) break;
						costs[v][i] = next_d;
					}
					costs[v][next_c] = next_d;
					PQ.push({-next_d, next_c, v});
				}
			}
		}

		return *min_element(costs[N].begin(), costs[N].end());
	}
};

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	int T;
	cin >> T;

	while (T--) {
		KCM travel;

		int res = travel.find();
		if (res == INF) cout << "Poor KCM\n";
		else cout << res << '\n';
	}

	return 0;
}