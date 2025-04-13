#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>

int main() {
	int K, C;
	int A, B;

	scanf("%d %d", &K, &C);

	while (C--) {
		int answer = 0;
		scanf("%d %d", &A, &B);

		if (A == B) answer = 1;
		else {
			int rem_round = B > A ? K - B : K - A + 1;
			int diff = B > A ? B - A : A - B;

			if (diff <= rem_round + 1) answer = 1;
		}

		printf("%d\n", answer);
	}

	return 0;
}