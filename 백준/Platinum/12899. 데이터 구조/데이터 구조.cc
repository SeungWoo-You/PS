#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

class SegTree {
private:
	int K = (int) pow(2, 21);
	vector<int> T = vector<int>(2 * K, 0);

public:
	void update(int p) {
		for (T[p += K]++; p > 1; p >>= 1)
			T[p >> 1]++;
	}

	int query(int X) {
		int p = 1;
		
		while (p < K) {
			T[p]--;
			if (T[p << 1] >= X) p <<= 1;
			else X -= T[p << 1], p = p << 1 | 1;
		}

		T[p]--;

		return p - K;
	}
};

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	SegTree ST;
	int N;
	cin >> N;

	while (N--) {
		int cmd, X;
		cin >> cmd >> X;

		if (cmd == 1) ST.update(X);
		else cout << ST.query(X) << '\n';
	}

	return 0;
}