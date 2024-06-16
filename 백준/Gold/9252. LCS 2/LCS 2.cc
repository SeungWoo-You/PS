#include <iostream>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	string A, B;
	cin >> A >> B;

	size_t M = A.size(), N = B.size();
	vector<vector<int>> table(M + 1, vector<int>(N + 1, 0));

	for (int i = 1; i <= M; i++) {
		for (int j = 1; j <= N; j++) {
			if (A[i - 1] == B[j - 1]) table[i][j] = table[i - 1][j - 1] + 1;
			else table[i][j] = max(table[i][j - 1], table[i - 1][j]);
		}
	}

	string LCS;

	for (int i = M, j = N; i > 0 && j > 0;) {
		if (table[i][j] > table[i][j - 1] && table[i][j - 1] == table[i - 1][j] && table[i - 1][j] == table[i - 1][j - 1]) {
			i--;
			j--;
			LCS += A[i];
		}
		else if (table[i][j] == table[i - 1][j] && table[i - 1][j] > table[i][j - 1]) i--;
		else j--;
	}

	cout << table[M][N] << '\n';
	if (LCS.size()) {
		reverse(LCS.begin(), LCS.end());
		cout << LCS;
	}
	return 0;
}