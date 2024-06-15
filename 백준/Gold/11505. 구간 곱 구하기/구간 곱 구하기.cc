#include <iostream>
#include <vector>

#define DIV 1000000007

using namespace std;

typedef long long LLT;

void update(vector<LLT>* nums, int N, int idx, LLT value) {
	for ((*nums)[idx += N] = value; idx > 1; idx >>= 1)
		(*nums)[idx >> 1] = ((*nums)[idx] * (*nums)[idx ^ 1]) % DIV;
}

LLT query(vector<LLT>* nums, int N, int l, int r) {
	LLT result = 1;

	for (l += N, r += N; l < r; l >>= 1, r >>= 1) {
		if (l & 1) result = (result * (*nums)[l++]) % DIV;
		if (r & 1) result = (result * (*nums)[--r]) % DIV;
	}

	return result % DIV;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int N, M, K;
	cin >> N >> M >> K;

	vector<LLT> nums(2 * N, 1);
	for (int i = N; i < 2 * N; i++) cin >> nums[i];

	for (int i = N - 1; i > 0; i--) nums[i] = (nums[i << 1] * nums[i << 1 | 1]) % DIV;

	for (int T = M + K; T > 0; T--) {
		int a, b;
		LLT c;
		cin >> a >> b >> c;

		if (a == 1) update(&nums, N, b - 1, c);
		else if (a == 2) cout << query(&nums, N, b - 1, (int) c) << '\n';
	}

	return 0;
}