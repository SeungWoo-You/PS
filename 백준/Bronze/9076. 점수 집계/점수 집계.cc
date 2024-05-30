#include <iostream>
#include <deque>
#include <numeric>
#include <algorithm>

using namespace std;

int main() {
	int T;
	const int N = 5;

	cin >> T;

	while (T--) {
		deque<int> dq(N);

		for (int i = 0; i < N; i++) cin >> dq[i];

		sort(dq.begin(), dq.end());
		dq.pop_front();
		dq.pop_back();

		if (dq.back() - dq.front() >= 4) printf("KIN\n");
		else {
			int score = accumulate(dq.begin(), dq.end(), 0);
			printf("%d\n", score);
		}
	}

	return 0;
}