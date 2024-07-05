#include <iostream>
#include <vector>

using namespace std;

class Josephus {
private:
	int N, K;
	vector<int> cnts;

	void build(int node, int s, int e) {
		if (s == e) {
			cnts[node] = 1;
			return;
		}

		int mid = (s + e) / 2;
		build(node << 1, s, mid);
		build(node << 1 | 1, mid + 1, e);
		cnts[node] = cnts[node << 1] + cnts[node << 1 | 1];
	}

public:
	Josephus(int N, int K) {
		this->N = N, this->K = K;
		cnts = vector<int>(4 * (N + 1), 0);

		build(1, 1, N);
	}

	int find(int node, int l, int r, int k) {
		cnts[node]--;
		if (l == r) return l;

		int mid = (l + r) / 2;
		if (cnts[node << 1] >= k)
			return find(node << 1, l, mid, k);
		else
			return find(node << 1 | 1, mid + 1, r, k - cnts[node << 1]);
	}
};

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	int N, K;
	cin >> N >> K;

	Josephus ST(N, K);
	int last = 1;

	cout << '<';
	for (int i = 0; i < N; i++) {
		int rem = N - i;
		last += K - 1;

		if (last % rem == 0) last = rem;
		else last %= rem;

		int x = ST.find(1, 1, N, last);
		
		if (i != N - 1) cout << x << ", ";
		else cout << x << '>';
	}

	return 0;
}