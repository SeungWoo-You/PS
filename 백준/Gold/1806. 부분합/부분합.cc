#include <iostream>
#include <vector>
#include <algorithm>

#define INF (~0U >> 2)

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int N, S;
	cin >> N >> S;

	vector<int> nums(N);
	for (int i = 0; i < N; i++) cin >> nums[i];

	int answer = INF;
	int i = 0, j = i;
	int total = nums[i];

	while (i < N && j < N) {
		if (total >= S) {
			answer = min(answer, j - i + 1);
			total -= nums[i++];
		}
		else {
			j++;
			if (j < N) total += nums[j];
		}
	}
	
	if (answer == INF) cout << 0;
	else cout << answer;

	return 0;
}