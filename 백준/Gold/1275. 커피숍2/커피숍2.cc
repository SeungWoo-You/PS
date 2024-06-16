#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

typedef long long LLT;

void update(vector<LLT>* nums, int N, int i, LLT val) {
	for ((*nums)[i += N] = val; i > 1; i >>= 1)
		(*nums)[i >> 1] = (*nums)[i] + (*nums)[i ^ 1];

	return;
}

LLT query(vector<LLT>* nums, int N, int l, int r) {
	LLT res = 0;
	
	for (l += N, r += N; l < r; l >>= 1, r >>= 1) {
		if (l % 2) res += (*nums)[l++];
		if (r % 2) res += (*nums)[--r];
	}
	
	return res;
}


int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int N, Q;
	cin >> N >> Q;

	vector<LLT> nums(2 * N);
	for (int i = N; i < 2 * N; i++) cin >> nums[i];

	for (int i = N - 1; i > 0; i--) nums[i] = nums[i << 1] + nums[i << 1 | 1];

	while (Q--) {
		int x, y, a;
		LLT b;
		cin >> x >> y >> a >> b;

		int i = min(x, y), j = max(x, y);

		cout << query(&nums, N, i - 1, j) << '\n';
		
		update(&nums, N, a - 1, b);
	}

	return 0;
}