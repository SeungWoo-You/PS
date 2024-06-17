#include <iostream>
#include <unordered_map>
#include <stack>
#include <vector>

using namespace std;

pair<int, int> find(unordered_map<int, unordered_map<int, int>>* graph, int N, int src) {
	pair<int, int> res = {src, 0};
	stack<pair<int ,int>> S;
	vector<bool> checked(N + 1, false);
	S.push({src, 0});
	checked[src] = true;

	while (!S.empty()) {
		int u = S.top().first, d = S.top().second;
		S.pop();

		if (d > res.second) {
			res.first = u;
			res.second = d;
		}

		for (auto& [v, w] : (*graph)[u]) {
			if (!checked[v]) {
				checked[v] = true;
				S.push({v, d + w});
			}
		}
	}

	return res;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int N;
	cin >> N;

	unordered_map<int, unordered_map<int, int>> graph;
	for (int i = 0; i < N - 1; i++) {
		int u, v, w;
		cin >> u >> v >> w;

		graph[u][v] = w;
		graph[v][u] = w;
	}

	pair<int, int> temp = find(&graph, N, 1);
	pair<int, int>res = find(&graph, N, temp.first);
	cout << res.second;
	
	return 0;
}