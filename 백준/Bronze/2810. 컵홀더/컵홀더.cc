#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>

#define MAX_N 51

int main() {
	int N;
	char seats[MAX_N];

	scanf("%d %s", &N, seats);

	int cup_num = N + 1;

	for (int i = 0; i < N; i++) {
		if (seats[i] == 'L') {
			cup_num--;
			i++;
		}
	}

	printf("%d", cup_num > N ? N : cup_num);

	return 0;
}