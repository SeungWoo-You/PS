#include <iostream>

#define MAX_N 50
#define MAX_M 50
#define MIN(x, y) (((x) > (y)) ? (y) : (x))

using namespace std;

int board[MAX_N][MAX_M] = {0};
char row[MAX_M + 1] = {0};

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	int N, M;
	cin >> N >> M;

	for (int i = 0; i < N; i++) {
		cin >> row;

		for (int j = 0; j < M; j++)
			board[i][j] = row[j] - '0';
	}

	int max_side = MIN(N, M);
	int answer = 0;

	for (int s = 1; s <= max_side; s++) {
		bool found = false;

		for (int i = 0; i <= N - s; i++) {
			for (int j = 0; j <= M - s; j++)
				if (board[i][j] == board[i + s - 1][j]
					&& board[i][j] == board[i][j + s - 1]
					&& board[i][j] == board[i + s - 1][j + s - 1]) {
					answer = s * s;
					found = true;
					break;
				}

			if (found) break;
		}
	}

	cout << answer;

	return 0;
}