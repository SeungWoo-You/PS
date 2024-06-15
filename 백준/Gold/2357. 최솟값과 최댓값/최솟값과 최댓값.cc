#include <iostream>
#include <vector>
#include <algorithm>

#define INF (~0U >> 2)

using namespace std;

typedef pair<int, int> PIIT;

PIIT query(vector<PIIT>* nums, int N, int l, int r) {
	PIIT result = {INF, -(int) INF};

	for (l += N, r += N; l < r; l >>= 1, r >>= 1) {
		if (l % 2) {
			result.first = min(result.first, (*nums)[l].first);
			result.second = max(result.second, (*nums)[l++].second);
		}
		if (r % 2) {
			result.first = min(result.first, (*nums)[--r].first);
			result.second = max(result.second, (*nums)[r].second);
		}
	}

	return result;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int N, M;
	cin >> N >> M;

	vector<PIIT> nums(2 * N, {INF, -(int) INF});
	for (int i = N; i < 2 * N; i++) {
		int x;
		cin >> x;

		nums[i] = {x, x};
	}

	for (int i = N - 1; i > 0; i--) {
		nums[i] = {
			min(nums[2 * i].first, nums[2 * i + 1].first),
			max(nums[2 * i].second, nums[2 * i + 1].second)
		};
	}

	while (M--) {
		int a, b;
		cin >> a >> b;

		PIIT result = query(&nums, N, a - 1, b);
		cout << result.first << ' ' << result.second << '\n';
	}

	return 0;
}