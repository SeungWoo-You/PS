#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>

#define NATURAL_SUM(N) (((long long) N) * (N + 1) / 2)

int main() {
	int N;
	long long sum = 0;

	scanf("%d", &N);

	for (int i = 0; i < N; i++) {
		int num;

		scanf("%d", &num);
		sum += num;
	}

	printf("%lld", sum - NATURAL_SUM(N - 1));

	return 0;
}