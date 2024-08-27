#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

typedef long long LLT;

class SegTree {
private:
	int K = pow(2, 20);
	vector<LLT> T = vector<LLT>(2 * K, 0);

public:
	void update(int p, LLT delta) {
		for (T[p += K] += delta; p > 1; p >>= 1)
			T[p >> 1] += delta;
	}

	int query(LLT target) {
		int p = 1;

		while (p < K) {
			T[p]--;
			if (T[p << 1] >= target)
				p <<= 1;
			else
				target -= T[p << 1], p = p << 1 | 1;
		}

		T[p]--;

		return p - K;
	}
};

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	int N;
	cin >> N;
	SegTree ST;
	
	while (N--) {
		int cmd;
		cin >> cmd;

		if (cmd == 1) {
			LLT target;
			cin >> target;
			cout << ST.query(target) << '\n';
		}
		else {
			int p;
			LLT delta;
			cin >> p >> delta;
			ST.update(p, delta);
		}
	}

	return 0;
}