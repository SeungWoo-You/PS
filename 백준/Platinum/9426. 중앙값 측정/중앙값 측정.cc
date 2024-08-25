#include <iostream>
#include <vector>

using namespace std;

typedef long long LLT;

class SegTree {
private:
	int M = 65536;
	vector<int> T;

public:
	SegTree() {
		
		T.resize(2 * M, 0);
	}

	void update(int p, int delta) {
		for (T[p += M] += delta; p > 1; p >>= 1)
			T[p >> 1] = T[p] + T[p ^ 1];
	}

	int query(int l, int r) {
		int res = 0;

		for (l += M, r += M; l < r; l >>= 1, r >>= 1) {
			if (l % 2) res += T[l++];
			if (r % 2) res += T[--r];
		}

		return res;
	}

	int find_median() {
		int p = 1;
		int target = (T[p] + 1) / 2;

		while (p < M) {
			if (T[p << 1] >= target) p <<= 1;
			else target -= T[p << 1], p = p << 1 | 1;
		}

		return p - M;
	}
};

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	int N, K;
	cin >> N >> K;
	
	SegTree ST;
	LLT res = 0;
	vector<int> arr(N, 0);

	for (int i = 0; i < K; i++) {
		cin >> arr[i];
		ST.update(arr[i], 1);
	}

	res += ST.find_median();

	for (int i = K; i < N; i++) {
		cin >> arr[i];
		ST.update(arr[i - K], -1);
		ST.update(arr[i], 1);
		res += ST.find_median();
	}

	cout << res;

	return 0;
}