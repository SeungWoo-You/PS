#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

#define MAX_LEN 1'000'000'000
#define MAX_ANS ~0U >> 1
#define MAX_N 1'000'000

static int snacks[MAX_N] = {0};
static int M, N;

int main() {
	int left = 1, right = -1;
	int ans = MAX_ANS;

	scanf("%d %d", &M, &N);

	for (register int i = 0; i < N; i++) {
		scanf("%d", &snacks[i]);

		if (snacks[i] > right)
			right = snacks[i];
	}

	while (left <= right) {
		int mid = (left + right) >> 1;
		int div = 0;

		for (register int n = 0; n < N; n++) {
			div += snacks[n] / mid;
			
			if (div >= M) break;
		}

		if (div >= M) {
			ans = mid;
			left = mid + 1;
		}
		else
			right = mid - 1;
	}

	if (ans == MAX_ANS)
		ans = 0;

	printf("%d", ans);

	return 0;
}