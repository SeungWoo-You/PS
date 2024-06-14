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
			int target = V[j] - V[i];
			int start = 0, end = two_sums.size() - 1;
			
			while (start <= end) {
				int mid = (start + end) / 2;

				if (two_sums[mid] > target) end = mid - 1;
				else if (two_sums[mid] < target) start = mid + 1;
				else {
					k = max(k, V[j]);
					break;
				}
			}
		}
	}

	cout << k;

	return 0;
}