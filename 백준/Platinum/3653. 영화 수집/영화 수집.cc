#include <iostream>
#include <vector>

using namespace std;

class DVDCollection {
private:
	int N, M, K;
	vector<int> movies;

public:
	DVDCollection(int N, int M) {
		this->N = N, this->M = M;
		K = N + M + 1;
		movies = vector<int>(2 * K, 0);

		for (int i = 1; i <= N; i++)
			update(i, 1);
	}

	void update(int p, int val) {
		for (movies[p += K] = val; p > 1; p >>= 1)
			movies[p >> 1] = movies[p] + movies[p ^ 1];
	}

	int query(int l, int r) {
		int res = 0;

		for (l += K, r += K; l < r; l >>= 1, r >>= 1) {
			if (l % 2) res += movies[l++];
			if (r % 2) res += movies[--r];
		}

		return res;
	}
};

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	int T;
	cin >> T;

	while (T--) {
		int N, M;
		cin >> N >> M;

		DVDCollection ST(N, M);
		int end = N + 1;
		vector<int> pos(N + 1);
		for (int i = 1; i <= N; i++)
			pos[i] = N - i + 1;

		while (M--) {
			int num;
			cin >> num;

			cout << ST.query(pos[num] + 1, end) << ' ';

			ST.update(pos[num], 0);
			ST.update(end, 1);
			pos[num] = end++;
		}

		cout << '\n';
	}

	return 0;
}