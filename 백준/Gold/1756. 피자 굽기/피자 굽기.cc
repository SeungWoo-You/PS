#include <iostream>

#define MAX_D 300'000
#define INF (~0U >> 2)

using namespace std;

int ovens[MAX_D];

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	int D, N;
	cin >> D >> N;

	int min_width = INF;

	for (int i = 0; i < D; i++) {
		cin >> ovens[i];
		
		if (i == 0) min_width = ovens[i];
		else if (ovens[i] > min_width) ovens[i] = min_width;
		else if (ovens[i] < min_width) min_width = ovens[i];
	}

	int last_pos = D - 1;

	for (int i = 0; i < N; i++) {
		if (last_pos < 0) break;

		int pizza;
		cin >> pizza;

		while (ovens[last_pos] < pizza) last_pos--;

		last_pos--;
	}

	cout << (last_pos < 0 ? 0 : last_pos + 2);

	return 0;
}