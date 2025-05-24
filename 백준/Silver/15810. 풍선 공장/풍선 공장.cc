#include <iostream>

#define MAX_N 1'000'000

using namespace std;

int times[MAX_N];

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	int N, M;
	cin >> N >> M;

	for (int i = 0; i < N; i++)
		cin >> times[i];

	long long left = 1, right = 1e12, res = 0;

	while (left <= right) {
		long long count = 0;
		long long mid = (left + right) >> 1;

		for (int i = 0; i < N; i++) {
			count += mid / times[i];
			if (count >= M) break;
		}

		if (count >= M) right = mid - 1, res = mid;
		else left = mid + 1;
	}

	cout << res;

	return 0;
}