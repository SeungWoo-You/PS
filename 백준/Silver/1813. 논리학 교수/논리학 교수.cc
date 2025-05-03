#include <iostream>

#define MAX(x, y) ((x) > (y) ? (x) : (y))

using namespace std;

int counts[51] = {0};

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	int N;
	cin >> N;

	int M = 0;

	for (int i = 0; i < N; i++) {
		int x;
		cin >> x;

		counts[x]++;

		M = MAX(M, x);
	}

	int answer = -1;

	for (int i = 0; i <= M; i++) {
		if (counts[i] == i) answer = i;
	}

	cout << answer;

	return 0;
}