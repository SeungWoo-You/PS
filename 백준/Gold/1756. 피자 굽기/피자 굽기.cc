#include <iostream>

#define MAX_N 300'000
#define MAX_D 300'000
#define INF (~0U >> 2)

using namespace std;

int ovens[MAX_D];
int pizzas[MAX_N];

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

	for (int i = 0; i < N; i++) cin >> pizzas[i];

	int last_pos = D, pid = 0;
	
	while (last_pos >= 1 && pid < N) {
		int pizza = pizzas[pid];
		
		if (pizza > ovens[0]) break;

		int start = 1, end = last_pos;

		while (start < end) {
			int mid = (start + end) >> 1;

			if (ovens[mid] < pizza) end = mid;
			else start = mid + 1;
		}

		last_pos = end - 1;
		pid++;
	}

	cout << (pid < N ? 0 : last_pos + 1);

	return 0;
}