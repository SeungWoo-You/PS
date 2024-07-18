#include <iostream>
#include <vector>
#include <algorithm>

#define INF (~0U >> 2)

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	int T;
	cin >> T;

	while (T--) {
		int N, M;
		cin >> N >> M;

		vector<vector<int>> dists(N + 1, vector<int>(N + 1, INF));
		for (int i = 1; i <= M; i++) {
			int a, b, c;
			cin >> a >> b >> c;
			dists[a][b] = c;
			dists[b][a] = c;
		}

		for (int i = 1; i <= N; i++)
			dists[i][i] = 0;

		for (int k = 1; k <= N; k++)
			for (int i = 1; i <= N; i++)
				for (int j = 1; j <= N; j++)
					dists[i][j] = min(dists[i][j], dists[i][k] + dists[k][j]);

		int K;
		cin >> K;

		vector<int> friends(K);
		for (int i = 0; i < K; i++) cin >> friends[i];

		int res = INF, ans = -1;
		for (int i = 1; i <= N; i++) {
			int total = 0;
			
			for (int k : friends)
				total += dists[i][k];

			if (total < res)
				ans = i, res = total;
		}

		cout << ans << '\n';
	}

	return 0;
}