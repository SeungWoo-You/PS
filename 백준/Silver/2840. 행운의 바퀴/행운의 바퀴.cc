#include <iostream>
#include <vector>
#include <unordered_set>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int N, K;
	cin >> N >> K;

	vector<char> wheel(N, '?');
	unordered_set<char> checked;
	int cur = 0;

	while (K--) {
		int S;
		char C;
		cin >> S >> C;

		cur = (cur + S) % N;
		
		if (wheel[cur] != '?') {
			if (wheel[cur] != C) {
				cout << '!';
				return 0;
			}
		}
		else {
			if (checked.count(C)) {
				cout << '!';
				return 0;
			}
			wheel[cur] = C;
			checked.insert(C);
		}
	}

	for (int i = 0; i < N; i++) {
		int j = (cur - i + N) % N;
		cout << wheel[j];
	}

	return 0;
}