#include <iostream>

#define MAX_STR_LEN 7

using namespace std;

int parts[10] = {1, 10, 100, 1'000, 10'000, 100'000, 1'000'000, 10'000'000, 100'000'000, 1'000'000'000};

int make_key(char color[MAX_STR_LEN]) {
	long key = 0;
	int place = 100000;

	for (int i = 0; color[i] != '\0'; i++) {
		key += color[i] * place;
		place /= 10;
	}

	switch (key) {
	case 10987970: return 0;
	case 11064000: return 1;
	case 12510000: return 2;
	case 12349131: return 3;
	case 13230029: return 4;
	case 11552200: return 5;
	case 11007100: return 6;
	case 12972926: return 7;
	case 11553100: return 8;
	case 13057610: return 9;
	default: return -1;
	}
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	long long answer = 0;

	for (int i = 0; i < 3; i++) {
		char color[MAX_STR_LEN];
		cin >> color;

		int key = make_key(color);
		if (i == 0) answer += (long long) (key * 10);
		else if (i == 1) answer += (long long) key;
		else answer *= (long long) parts[key];
	}

	cout << answer;

	return 0;
}