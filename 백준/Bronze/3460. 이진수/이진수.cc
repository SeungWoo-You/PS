#include <iostream>

int main() {
	int T;

	scanf("%d", &T);
	while (T--) {
		int n;
		scanf("%d", &n);
		for (int i = 0; n != 0; i++) {
			if (n & 1) printf("%d ", i);
			n >>= 1;
		}
		printf("\n");
	}

	return 0;
}