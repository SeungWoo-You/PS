#include <iostream>
#include <vector>
#include <climits>
#include <queue>

using namespace std;

class Tour {
private:
	int N, M, K;
	vector<vector<pair<int, int>>> G;
	vector<priority_queue<int>> dists;
public:
	int root = 1;

	Tour() {
		cin >> N >> M >> K;
		G.resize(N + 1);

		for (int i = 0; i < M; i++) {
			int a, b, c;
			cin >> a >> b >> c;
			G[a].push_back({b, c});
		}
	}

	void find() {
		dists.resize(N + 1);

		priority_queue<pair<int, int>> PQ;
		PQ.push({0, root});
		dists[root].push(0);

		while (!PQ.empty()) {
			int d = -PQ.top().first, u = PQ.top().second;
			PQ.pop();

			for (auto [v, w] : G[u]) {
				int D = d + w;

				if (dists[v].size() < K) {
					dists[v].push(D);
					PQ.push({-D, v});
				}
				else if (dists[v].top() > D) {
					dists[v].pop();
					dists[v].push(D);
					PQ.push({-D, v});
				}
			}
		}
	}

	void print() {
		for (int i = 1; i <= N; i++) {
			if (dists[i].size() < K)
				cout << -1;
			else
				cout << dists[i].top();
			cout << '\n';
		}
	}
};

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	Tour T;
	T.find();
	T.print();

	return 0;
}