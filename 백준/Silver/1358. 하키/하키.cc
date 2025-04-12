#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>

#define EPSILON 1e-10
#define SQUARE(x) ((x) * (x))
#define ABS(x) ((x) > 0 ? (x) : -(x))


double calc_dist(double A[2], int B[2]) {
	return SQUARE(A[0] - B[0]) + SQUARE(A[1] - B[1]);
}


int main() {
	int W, H, X, Y, P;
	int count = 0;
	int pos[2];
	
	scanf("%d %d %d %d %d", &W, &H, &X, &Y, &P);

	double R = H / 2.0;
	double r_center_left[2] = {(double) X, Y + R}, r_center_right[2] = {(double) X + W, Y + R};

	for (int i = 0; i < P; i++) {
		scanf("%d %d", &pos[0], &pos[1]);

		if (X <= pos[0] && pos[0] <= X + W
			&& Y <= pos[1] && pos[1] <= Y + H) {
			count++;
			continue;
		}

		double left_diff = calc_dist(r_center_left, pos) - EPSILON;

		if (ABS(left_diff) < SQUARE(R)) {
			count++;
			continue;
		}

		double right_diff = calc_dist(r_center_right, pos) - EPSILON;

		if (ABS(right_diff) < SQUARE(R)) {
			count++;
			continue;
		}
	}

	printf("%d", count);

	return 0;
}