#include <iostream>

using namespace std;

bool arr[1'000'002] = {false};

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	int N, M;

	cin >> N >> M;

	int count = 0;

	for (int i = 1; i <= N; i++) {
		cin >> arr[i];

		if (arr[i] && !arr[i - 1])
			count++;
	}

	while (M--) {
		bool cmd;

		cin >> cmd;

		if (cmd) {
			int idx;

			cin >> idx;

			if (arr[idx]) continue;

			arr[idx] = true;

			if (arr[idx - 1] && arr[idx + 1]) count--;
			else if (!arr[idx - 1] && !arr[idx + 1]) count++;
		}
		else
			cout << count << '\n';
	}

	return 0;
}