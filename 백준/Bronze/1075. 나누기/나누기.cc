#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>

int main() {
	int N, F;
	scanf("%d %d", &N, &F);

	int target = (N / 100 * 100) % F;
	printf("%02d", (F - target) % F);

	return 0;
}