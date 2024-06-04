#include <iostream>
#include <vector>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	
	int N, M;
	cin >> N >> M;

	vector<int> nums(N);
	for (int i = 0; i < N; i++) cin >> nums[i];
	
	int count = 0, total =0;
	int i = 0, j = i;

	while (i < N) {
		if (total < M) {
			if (j == N) break;
			total += nums[j];
			j += 1;
		}
		else {
			if (total == M) count += 1;
			total -= nums[i];
			i += 1;
		}
	}

	cout << count;

	return 0;
}