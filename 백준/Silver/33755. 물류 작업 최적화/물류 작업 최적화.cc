#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>

#define STOCK 300'000
#define MAX(x, y) ((x) > (y) ? (x) : (y))


long cumulated[STOCK][2];
int stocks[STOCK];
long answer[STOCK];

int main() {
	int N;

	scanf("%d", &N);

	for (int i = 0; i < N; i++)
		scanf("%d", &stocks[i]);

	if (N == 1) {
		printf("%d", stocks[0]);
		
		return 0;
	}

	for (int i = 0; i < N; i++)
		for (int j = 0; j < 2; j++)
			cumulated[i][j] = -2000;


	cumulated[0][0] = stocks[0];

	for (int i = 1; i < N; i++)
		cumulated[i][0] = MAX(cumulated[i - 1][0] + stocks[i], stocks[i]);

	cumulated[N - 1][1] = (long) stocks[N - 1];

	for (int i = N - 2; i >= 0; i--)
		cumulated[i][1] = MAX(cumulated[i + 1][1] + stocks[i], stocks[i]);


	for (int i = 0; i < N; i++) {
		long M1 = MAX(cumulated[i][0], cumulated[i][1]);

		if (i == 0)
			answer[i] = MAX(M1, cumulated[i][0] + cumulated[i + 1][1]);
		else if (i == N - 1)
			answer[i] = MAX(M1, cumulated[i - 1][0] + cumulated[i][1]);
		else {
			long M2 = MAX(cumulated[i][0] + cumulated[i + 1][1], cumulated[i - 1][0] + cumulated[i][1]);
			answer[i] = MAX(M1, M2);
		}
	}

	for (int i = 0; i < N; i++)
		printf("%ld ", answer[i]);

	return 0;
}