#include <iostream>
#include <vector>

using namespace std;

typedef long long ll_t;

struct VecN {
	vector<ll_t> nums;
	int N;
};

void update(VecN* V, int idx, ll_t value) {
	int i = idx + V->N;
	V->nums[i] = value;

	for (; i > 1; i >>= 1) V->nums[i >> 1] = V->nums[i] + V->nums[i ^ 1];

	return;
}

ll_t query(VecN* V, int l, int r) {
	ll_t result = 0;
	
	for (l += V->N, r += V->N; l < r; l >>= 1, r >>= 1) {
		if (l % 2) result += V->nums[l++];
		if (r % 2) result += V->nums[--r];
	}

	return result;
}


int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int N, M, K;
	cin >> N >> M >> K;

	VecN V = {vector<ll_t>(2 * N), N};
	for (int i = N; i < 2 * N; i++) cin >> V.nums[i];

	for (int i = N - 1; i > 0; i--) V.nums[i] = V.nums[2 * i] + V.nums[2 * i + 1];

	for (int _ = 0; _ < M + K; _++) {
		int a, b;
		ll_t c;
		cin >> a >> b >> c;
		
		if (a == 1) update(&V, b - 1, c);
		else if (a == 2) cout << query(&V, b - 1, (int) c) << '\n';
	}

 	return 0;
}