#include <iostream>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int N;
	cin >> N;

	vector<int> V(N);
	for (int i = 0; i < N; i++) cin >> V[i];

	vector<int> two_sums;
	for (int i = 0; i < N; i++)
		for (int j = i; j < N; j++)
			two_sums.push_back(V[i] + V[j]);

	sort(V.begin(), V.end());
	sort(two_sums.begin(), two_sums.end());

	int k = 0;

	for (int i = 0; i < N; i++) {
		for (int j = i; j < N; j++) {
			if (binary_search(two_sums.begin(), two_sums.end(), V[j] - V[i])) k = max(k, V[j]);
		}
	}

	cout << k;

	return 0;
}