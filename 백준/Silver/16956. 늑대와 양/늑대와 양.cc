#include <iostream>

#define MAX_R 500
#define MAX_C 500

struct Point {
	int x;
	int y;
};

char field[MAX_R + 1][MAX_C + 1];
Point wolves[MAX_R * MAX_C];
int wolves_count = 0;


using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	int R, C;
	cin >> R >> C;

	for (int i = 0; i < R; i++)
		for (int j = 0; j < C; j++) {
			cin >> field[i][j];
			if (field[i][j] == 'W') {
				wolves[wolves_count].x = i;
				wolves[wolves_count].y = j;
				wolves_count++;
			}
		}

	int Dx[4] = {-1, 0, 0, 1};
	int Dy[4] = {0, -1, 1, 0};
	int answer = 1;

	for (int wid = 0; wid < wolves_count; wid++) {
		Point* wolf = &wolves[wid];

		for (int d = 0; d < 4; d++) {
			int x = wolf->x + Dx[d], y = wolf->y + Dy[d];

			if (0 <= x && x < R && 0 <= y && y < C) {
				if (field[x][y] == 'S') {
					answer = 0;
					break;
				}
				else if (field[x][y] == '.')
					field[x][y] = 'D';
			}
		}
	}

	cout << answer << '\n';

	if (answer)
		for (int i = 0; i < R; i++) {
			for (int j = 0; j < C; j++)
				cout << field[i][j];
			cout << '\n';
		}

	return 0;
}