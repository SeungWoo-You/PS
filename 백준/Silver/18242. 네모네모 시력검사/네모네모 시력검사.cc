#include <iostream>

using namespace std;

char rect[101][101];

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	int N, M;
	cin >> N >> M;
	
	int TL[2] = {-1, -1};
	int DR[2] = {-1, -1};

	for (int i = 0; i < N; i++)
		for (int j = 0; j < M; j++) {
			cin >> rect[i][j];

			if (rect[i][j] == '#') {
				if (TL[0] == -1)
					TL[0] = i, TL[1] = j;
				else
					DR[0] = i, DR[1] = j;
			}
		}

	int center[2] = {(TL[0] + DR[0]) >> 1, (TL[1] + DR[1]) >> 1};
	int X[4] = {center[0], TL[0], DR[0], center[0]};
	int Y[4] = {TL[1], center[1], center[1], DR[1]};
	char D[4][6] = {"LEFT", "UP", "DOWN", "RIGHT"};


	for (int d = 0; d < 4; d++) {
		int x = X[d], y = Y[d];

		if (rect[x][y] == '.') {
			cout << D[d];

			return 0;
		}
	}

	return 0;
}