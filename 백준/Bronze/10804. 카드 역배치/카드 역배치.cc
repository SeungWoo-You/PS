#include <iostream>

#define MAX_N 21

using namespace std;

void swap(int* a, int* b) {
	int temp = *a;
	*a = *b;
	*b = temp;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	int cards[MAX_N] = {0};

	for (int i = 1; i < MAX_N; i++) cards[i] = i;

	for (int t = 0; t < 10; t++) {
		int s, e;
		cin >> s >> e;

		int D = (e - s + 1) >> 1;

		for (int diff = 0; diff < D; diff++)
			swap(&cards[s + diff], &cards[e - diff]);
	}

	for (int i = 1; i < MAX_N; i++)
		cout << cards[i] << ' ';

	return 0;
}