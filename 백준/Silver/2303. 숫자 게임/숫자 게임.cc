#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>

#define MAX_CARD 5
#define MAX_PLAYER 1000

int result[10] = {0};
int selected[3];
int cards[MAX_CARD];

void combi(int start, int r, int pid, int sum) {
	if (r == 3) {
		int idx = sum % 10;

		if (result[idx] < pid)
			result[idx] = pid;

		return;
	}

	for (int i = start; i < MAX_CARD; i++) {
		sum += cards[i];
		combi(i + 1, r + 1, pid, sum);
		sum -= cards[i];
	}
}

int main() {
	int N;

	scanf("%d", &N);
	int pid = 0;

	while (N--) {
		pid++;

		for (int i = 0; i < MAX_CARD; i++)
			scanf("%d", &cards[i]);

		combi(0, 0, pid, 0);
	}

	for (int i = 9; i >= 0; i--)
		if (result[i]) {
			printf("%d", result[i]);
			break;
		}

	return 0;
}