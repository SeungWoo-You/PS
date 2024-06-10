#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdlib>

#define INF (~0U >> 2);

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int N;
	cin >> N;

	vector<int> solutions(N);
	for (int i = 0; i < N; i++) cin >> solutions[i];

	sort(solutions.begin(), solutions.end());

	int p1 = 0, p2 = N - 1;
	int spec = 2 * INF;
	int s1 = solutions[p1], s2 = solutions[p2];

	while (p1 < p2) {
		int m1 = solutions[p1], m2 = solutions[p2];
		int mixed = m1 + m2;

		if (mixed < 0) p1 += 1;
		else if (mixed > 0) p2 -= 1;
		else {
			s1 = m1;
			s2 = m2;
			break;
		}

		if (abs(m1 + m2) < spec) {
			s1 = m1;
			s2 = m2;
			spec = abs(m1 + m2);
		}
	}

	cout << s1 << ' ' << s2;

	return 0;
}