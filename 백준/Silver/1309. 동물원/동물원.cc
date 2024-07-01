#include <iostream>
#include <vector>

#define DIV 9901
#define XX 0
#define OX 1
#define XO 2

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	int N;
	cin >> N;

	vector<vector<int>> cages(N + 1, vector<int>(3, 0));
	cages[1][XX] = 1, cages[1][OX] = 1, cages[1][XO] = 1;

	for (int n = 2; n <= N; n++) {
		cages[n][XX] = (cages[n - 1][XX] + cages[n - 1][OX] + cages[n - 1][XO]) % DIV;
		cages[n][OX] = (cages[n - 1][XX] + cages[n - 1][XO]) % DIV;
		cages[n][XO] = (cages[n - 1][XX] + cages[n - 1][OX]) % DIV;
	}

	cout << (cages[N][XX] + cages[N][XO] + cages[N][OX]) % DIV << '\n';

	return 0;
}