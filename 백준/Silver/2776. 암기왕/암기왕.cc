#include <iostream>
#include <unordered_set>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int T;
	cin >> T;

	while (T--) {
		int N;
		cin >> N;

		unordered_set<int> note1;
		for (int i = 0; i < N; i++) {
			int x;
			cin >> x;
			note1.insert(x);
		}

		int M;
		cin >> M;
		unordered_set<int> note2;
		for (int i = 0; i < M; i++) {
			int x;
			cin >> x;
			if (note1.count(x)) cout << 1 << '\n';
			else cout << 0 << '\n';
		}
	}

	return 0;
}