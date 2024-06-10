#include <iostream>
#include <vector>
#include <numeric>

#define INF (~0U >> 2);

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int N, M;
	cin >> N >> M;

	vector<vector<int>> relations;
	relations.resize(N + 1, vector<int>(N + 1, 0));

	for (int k = 1; k <= M; k++) {
		int i, j;
		cin >> i >> j;

		relations[i][j] = 1;
		relations[j][i] = 1;
	}

	for (int i = 1; i <= N; i++) {
		for (int j = 1; j <= N; j++)
			if (relations[i][j] == 0)
				relations[i][j] = INF;
		relations[i][i] = 0;
	}

	for (int k = 1; k <= N; k++)
		for (int i = 1; i <= N; i++)
			for (int j = 1; j <= N; j++)
				relations[i][j] = min(relations[i][j], relations[i][k] + relations[k][j]);

	int answer = 0, value = INF;

	for (int i = 1; i <= N;i++) {
		int total = accumulate(relations[i].begin(), relations[i].end(), 0);
		if (total < value) {
			answer = i;
			value = total;
		}
	}

	cout << answer;

	return 0;
}