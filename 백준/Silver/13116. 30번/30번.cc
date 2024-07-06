#include <iostream>
#include <algorithm>
#include <cstdlib>

using namespace std;

pair<int, int> find_depths(int A, int B) {
	pair<int, int> res = {0, 0};

	for (int d = 0; A > 0; A >>= 1) res.first = d++;
	for (int d = 0; B > 0; B >>= 1) res.second = d++;

	return res;
}

int find_lca(int A, int B) {
	pair<int, int> depths = find_depths(A, B);

	if (depths.first < depths.second) swap(A, B);

	for (int diff = abs(depths.first - depths.second); diff > 0; diff--)
		A >>= 1;

	while (A != B) A >>= 1, B >>= 1;

	return A;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	int T;
	cin >> T;

	while (T--) {
		int A, B;
		cin >> A >> B;
		cout << 10 * find_lca(A, B) << '\n';
	}

	return 0;
}