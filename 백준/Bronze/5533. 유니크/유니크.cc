#include <iostream>

#define MAX_N 200
#define TURN 3

using namespace std;

int players[MAX_N][TURN];
int counts[101][TURN] = {0};

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	int N;
	cin >> N;

	for (int i = 0; i < N; i++) {
		cin >> players[i][0] >> players[i][1] >> players[i][2];

		for (int j = 0; j < TURN; j++)
			counts[players[i][j]][j]++;
	}

	for (int i = 0; i < N; i++) {
		int total = 0;

		for (int j = 0; j < TURN; j++)
			if (counts[players[i][j]][j] == 1) total += players[i][j];

		cout << total << '\n';
	}

	return 0;
}