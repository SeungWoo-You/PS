#include <iostream>

#define MAX_N 20
#define MAX_C 1000
#define MAX(x, y) ((x) > (y) ? (x) : (y))

using namespace std;

int costs[MAX_N], clients[MAX_N];
int dp[MAX_C * 100 + 1] = {0};

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	int C, N;
	cin >> C >> N;

	for (int i = 0; i < N; i++)
		cin >> costs[i] >> clients[i];

	for (int c = 1; c <= MAX_C * 100; c++)
		for (int n = 0; n < N; n++)
			if (c - costs[n] >= 0)
				dp[c] = MAX(dp[c], dp[c - costs[n]] + clients[n]);

	for (int c = 1; c <= MAX_C * 100; c++)
		if (dp[c] >= C) {
			cout << c;
			break;
		}

	return 0;
}