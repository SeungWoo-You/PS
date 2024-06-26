#include <iostream>
#include <vector>

using namespace std;

typedef long long LLT;

class Tree {
private:
	int N;
	vector<LLT> D, T;
public:
	Tree(int N) {
		this->N = N;
		this->D = vector<LLT>(2 * N, 0);
		this->T = vector<LLT>(2 * N, 0);

		for (int i = N; i < 2 * N; i++) cin >> T[i];
		for (int i = N - 1; i > 0; i--) T[i] = T[i << 1] + T[i << 1 | 1];
	}

	void apply(int p, LLT val, int k) {
		for (D[p] += val; p > 1; p >>= 1)
			T[p >> 1] += val * k;
	}

	void modify(int l, int r, LLT val) {
		if (val == 0) return;

		int k = 1;

		for (l += N, r += N; l < r; l >>= 1, r >>= 1, k <<= 1) {
			if (l % 2) apply(l++, val, k);
			if (r % 2) apply(--r, val, k);
		}
	}

	LLT calc(int p, int k) {
		LLT res = T[p];

		for (; p > 0; p >>= 1) res += D[p] * k;

		return res;
	}

	LLT query(int l, int r) {
		LLT res = 0;
		int k = 1;

		for (l += N, r += N; l < r; l >>= 1, r >>= 1, k <<= 1) {
			if (l % 2) res += calc(l++, k);
			if (r % 2) res += calc(--r, k);
		}

		return res;
	}
};

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int N, M, K;
	cin >> N >> M >> K;

	Tree ST(N);
	int trial = M + K;

	while (trial--) {
		int a, b, c;
		cin >> a >> b >> c;

		if (a == 1) {
			LLT d;
			cin >> d;

			ST.modify(b - 1, c, d);
		}
		else {
			cout << ST.query(b - 1, c) << '\n';
		}
	}

	return 0;
}