#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

constexpr int INF = (~0U >> 2);

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int N;
	cin >> N;

	vector<vector<int>> graph;
	graph.resize(N, vector<int>(N));

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			int m;
			cin >> m;

			if (m == 0) m = INF;

			graph[i][j] = m;
		}
	}

	for (int k = 0; k < N; k++)
		for (int i = 0; i < N; i++)
			for (int j = 0; j < N; j++)
				graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j]);

	for (vector<int> gp : graph) {
		for (int x : gp) {
			if (x == INF) cout << 0 << ' ';
			else cout << 1 << ' ';
		}
		cout << '\n';
	}

	return 0;
}