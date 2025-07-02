#include <iostream>

#define MAX_N 100

using namespace std;

int scores[MAX_N] = {0};

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	int N;
	cin >> N;

	for (int i = 0; i < N; i++) cin >> scores[i];

	int count = 0;

	for (int prev = N - 1, now = N - 2; now >= 0; prev--, now--)
		if (scores[prev] <= scores[now]) {
			count += scores[now] - scores[prev] + 1;
			scores[now] = scores[prev] - 1;
		}

	cout << count;

	return 0;
}