#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>

char map[1002][1002] = {0};
int Dx[8] = {-1, -1, -1, 0, 0, 1, 1, 1};
int Dy[8] = {-1, 0, 1, -1, 1, -1, 0, 1};
char line[1002] = {0};

int main() {
	int N;

	scanf("%d", &N);

	for (int i = 0; i < N; i++)
		for (int j = 0; j < N; j++)
			map[i][j] = '0';

	for (int i = 0; i < N; i++) {
		scanf("%s", line);
		
		for (int j = 0; j < N; j++) {
			if (line[j] == '.') continue;

			map[i][j] = '*';

			for (int d = 0; d < 8; d++) {
				int x = i + Dx[d], y = j + Dy[d];

				if (0 <= x && x < N && 0 <= y && y < N && '0' <= map[x][y] && map[x][y] <= '9') {
					map[x][y] += (line[j] - '0');

					if (map[x][y] > '9') map[x][y] = 'M';
				}
			}
		}
	}

	for (int i = 0; i < N; i++)
		printf("%s\n", map[i]);

	return 0;
}