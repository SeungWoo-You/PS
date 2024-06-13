#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int N;
	cin >> N;

	vector<int> cards(N + 1), costs(N + 1, 0);
	for (int i = 1; i <= N; i++) cin >> cards[i];

	for (int i = 1; i <= N; i++)
		for (int j = 1; j <= i; j++) {
			int c = cards[j] + costs[i - j];
			costs[i] = max(costs[i], c);
		}

	cout << costs[N];

	return 0;
}