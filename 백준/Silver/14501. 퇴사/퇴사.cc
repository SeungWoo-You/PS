#include <iostream>
#include <vector>
#include <algorithm>

#define MAX_PREV 5

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int N;
	cin >> N;

	vector<int> T(N + 1), P(N + 1), A(N + 1, 0);
	for (int i = 1; i <= N; i++) cin >> T[i] >> P[i];

	for (int today = 1; today <= N; today++) {
		for (int prev = 0; prev < MAX_PREV; prev++) {
			int pday = today - prev;
			if (pday <= 0) break;

			if (T[pday] - 1 == prev) A[today] = max(A[today], A[pday - 1] + P[pday]);
			else A[today] = max(A[today], A[today - 1]);
		}
	}

	cout << A[N];

	return 0;
}