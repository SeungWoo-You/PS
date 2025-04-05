#define _CRT_SECURE_NO_WARNINGS

#include <stdio.h>

#define MAX_U 10'000

struct User {
	int id;
	char name[11];
};

int counts[MAX_U + 1] = {0};
User users[MAX_U + 1];

int main() {
	int U, N;
	int cid = -1, min_count = 20'000;

	scanf("%d %d", &U, &N);

	for (int idx = 0; idx < N; idx++) {
		User user;
		user.id = idx;
		int cost;

		scanf("%s %d", user.name, &cost);

		if (counts[cost] == 0)
			users[cost] = user;

		counts[cost]++;
	}

	for (int c = 1; c <= U; c++) {
		if (counts[c] == 0) continue;

		if (min_count > counts[c]) {
			min_count = counts[c];
			cid = c;
		}
	}

	printf("%s %d", users[cid].name, cid);

	return 0;
}