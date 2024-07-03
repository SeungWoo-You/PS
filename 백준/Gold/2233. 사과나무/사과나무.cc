#include <iostream>
#include <vector>
#include <string>
#include <stack>
#include <algorithm>

using namespace std;

class Tree {
private:
	int N, K = 0;
	vector<int> idx_mapping;
	vector<vector<int>> parents;
	vector<int> depths;
	string binary;

	void build() {
		stack<pair<int, int>> S;

		S.push({root, 1});
		depths[root] = 1;
		apples[root].first = 1;
		idx_mapping[1] = root;

		for (int i = 1, node = root; i < 2 * N; i++) {
			if (binary[i] == '0') {
				node++;
				int p = S.top().first;
				int d = S.top().second + 1;
				S.push({node, d});

				parents[node][0] = p;
				depths[node] = d;
				apples[node].first = i + 1;
				idx_mapping[i + 1] = node;
			}
			else {
				int x = S.top().first;
				S.pop();

				apples[x].second = i + 1;
				idx_mapping[i + 1] = x;
			}
		}

		init_parents();
	}

	void init_parents() {
		for (int k = 1; k <= K; k++)
			for (int i = 1; i <= N; i++)
				if (parents[i][k - 1] != 0)
					parents[i][k] = parents[parents[i][k - 1]][k - 1];
	}

public:
	int root = 1;
	vector<pair<int, int>> apples;

	Tree() {
		cin >> N;

		for (int temp = N; temp > 0; temp >>= 1) K++;
		apples = vector<pair<int, int>>(N + 1, {0, 0});
		parents = vector<vector<int>>(N + 1, vector<int>(K + 1, 0));
		depths = vector<int>(N + 1, 0);
		idx_mapping = vector<int>(2 * N + 1, 0);

		cin >> binary;

		build();
	}

	int find(int l, int r) {
		int u = idx_mapping[l], v = idx_mapping[r];

		if (depths[u] < depths[v]) swap(u, v);

		for (int diff = depths[u] - depths[v], i = 0; diff > 0; diff >>= 1, i++)
			if (diff % 2) u = parents[u][i];

		if (u != v) {
			for (int k = K; k >= 0; k--)
				if (parents[u][k] != parents[v][k])
					u = parents[u][k], v = parents[v][k];
			u = parents[u][0];
		}

		return u;
	}
};

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	Tree T;

	int l, r;
	cin >> l >> r;

	int rotten = T.find(l, r);

	cout << T.apples[rotten].first << ' ' << T.apples[rotten].second;

	return 0;
}