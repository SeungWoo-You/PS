#include <iostream>
#include <vector>

#define DIV 1000000007
#define SIZE 200001

using namespace std;

typedef long long LLT;

class SegTree {
private:
	vector<int> cnts;
	vector<LLT> T;

public:
	SegTree() {
		cnts = vector<int>(2 * SIZE, 0);
		T = vector<LLT>(2 * SIZE, 0);
	}

	void update(int i) {
		int i0 = i;

		for (cnts[i += SIZE] += 1, T[i] = T[i] + i0; i > 1; i >>= 1) {
			cnts[i >> 1] = cnts[i] + cnts[i ^ 1];
			T[i >> 1] = T[i] + T[i ^ 1];
		}
	}

	pair<LLT, int> query(int l, int r) {
		LLT res = 0;
		int c = 0;

		for (l += SIZE, r += SIZE; l < r; l >>= 1, r >>= 1) {
			if (l % 2) {
				res = res + T[l];
				c += cnts[l++];
			}
			if (r % 2) {
				c += cnts[--r];
				res = res + T[r];
			}
		}

		return {res, c};
	}
};

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	int N;
	cin >> N;

	SegTree ST;
	LLT res = 1;

	for (int i = 0; i < N; i++) {
		int x;
		cin >> x;

		ST.update(x);

		if (i == 0) continue;

		pair<LLT, int> left = ST.query(0, (int) x), right = ST.query(x + 1, SIZE);
		LLT temp = 0;

		if (left.second)
			temp += ((LLT) x * left.second - left.first) % DIV;
		if (right.second)
			temp += (right.first - (LLT) x * right.second) % DIV;
		if (temp != 0)
			res = (res * temp) % DIV;

		if (i == N - 1) {
			pair<LLT, int> last = ST.query(x, x + 1);
			if (last.second == N)
				res = 0;
		}
	}

	cout << res;

	return 0;
}