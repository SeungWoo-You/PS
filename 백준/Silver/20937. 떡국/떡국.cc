#include <iostream>

using namespace std;

int counts[50001] = {0};

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	int N;
	cin >> N;

	int answer = 0;

	for (int i = 0; i < N; i++) {
		int x;
		cin >> x;

		counts[x]++;

		if (counts[x] > answer)
			answer = counts[x];
	}

	cout << answer;

	return 0;
}