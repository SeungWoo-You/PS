#include <iostream>
#include <vector>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	int N, K;
	cin >> N >> K;

	vector<int> coins(N + 1, 0), counts(K + 1, 0);
	counts[0] = 1;

	for (int i = 1; i <= N; i++) {
		int v;
		cin >> v;
		coins[i] = v;
	}

	for (int i = 1; i <= N;i++)
		for (int k = coins[i]; k <= K; k++)
				counts[k] = counts[k] + counts[k - coins[i]];

	cout << counts[K];

	return 0;
}