#include <iostream>
#include <vector>

#define DIV 1000000000

using namespace std;

typedef long long LLT;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	int N, K;
	cin >> N >> K;

	vector<vector<LLT>> DP(K + 1, vector<LLT>(N + 1, 0));
	for (int k = 0; k <= K; k++)DP[k][0] = 1;
	for (int i = 1; i <= N; i++) DP[1][i] = 1;
	
	for (int i = 1; i <= N; i++)
		for (int k = 1; k <= K; k++)
			DP[k][i] = (DP[k - 1][i] + DP[k][i - 1]) % DIV;

	cout << DP[K][N];

	return 0;
}