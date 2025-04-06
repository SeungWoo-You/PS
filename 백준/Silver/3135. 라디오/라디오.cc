#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>

#define ABS(x) ((x) > 0 ? (x) : -(x))

int main() {
	int A, B, N;

	scanf("%d %d %d", &A, &B, &N);
	int count = ABS(A - B);


	for (int i = 0; i < N; i++) {
		int btn;

		scanf("%d", &btn);

		int temp = ABS(btn - B) + 1;

		if (temp < count) count = temp;
	}

	printf("%d", count);

	return 0;
}