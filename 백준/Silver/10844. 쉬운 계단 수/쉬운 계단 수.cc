#include <iostream>
#include <vector>
#include <numeric>

#define DIV 1000000000
#define DIGIT 10

using namespace std;

typedef long long LLT;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	int N;
	cin >> N;

	vector<vector<LLT>> DP(N + 1, vector<LLT>(DIGIT, 0));
	for (int j = 1; j < DIGIT; j++) DP[1][j] = 1;

	for (int i = 2; i <= N; i++)
		for (int j = 0; j < DIGIT; j++) {
			if (j + 1 < DIGIT)
				DP[i][j] = (DP[i][j] + DP[i - 1][j + 1]) % DIV;
			if (j - 1 >= 0)
				DP[i][j] = (DP[i][j] + DP[i - 1][j - 1]) % DIV;
		}

	cout << (accumulate(DP[N].begin(), DP[N].end(), (LLT) 0)) % DIV;

	return 0;
}