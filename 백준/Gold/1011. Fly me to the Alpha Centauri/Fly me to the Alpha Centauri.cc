#include <iostream>

using namespace std;

int ceil(int num, int div) {
	return num / div + (num % div ? 1 : 0);
}

int find_k(int dist) {
	int left = 1, right = 46341;

	while (left < right) {
		int mid = (left + right) >> 1;

		if (ceil(dist, mid) > mid + 1) left = mid + 1;
		else right = mid;
	}

	return right;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	int T;
	cin >> T;

	while (T--) {
		int src, dst;
		cin >> src >> dst;

		int dist = dst - src;
		int k = find_k(dist);

		cout << ((k << 1) - (int) (ceil(dist, k) <= k)) << '\n';
	}

	return 0;
}