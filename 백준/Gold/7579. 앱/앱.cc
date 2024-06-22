#include <iostream>
#include <vector>
#include <array>
#include <algorithm>

#define SIZE 10001

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int N, M;
	cin >> N >> M;

	vector<int> mems(N + 1), costs(N + 1);
	for (int i = 1; i <= N; i++) cin >> mems[i];
	for (int i = 1; i <= N; i++) cin >> costs[i];

	vector<vector<int>> table(N + 1, vector<int>(SIZE, 0));

	for (int i = 1; i <= N; i++) {
		for (int w = 0; w < SIZE; w++) {
			if (costs[i] > w) table[i][w] = table[i - 1][w];
			else table[i][w] = max(table[i - 1][w], table[i - 1][w - costs[i]] + mems[i]);
		}
	}

	for (int w = 0; w < SIZE; w++) {
		if (table[N][w] >= M) {
			cout << w << '\n';
			return 0;
		}
	}

	return 0;
}