#include <iostream>

#define MAX_N 100'000

using namespace std;

int nums[MAX_N];

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	int N, K;
	cin >> N >> K;
	
	int M = 0;
	int left = 0, right = -1;

	for (int i = 0; i < N; i++) {
		cin >> nums[i];

		if (right < K - 1) M += nums[++right];
	}

	int sum = M;

	for (int i = K; i < N; i++) {
		sum += nums[++right] - nums[left++];

		if (sum > M) M = sum;
	}

	cout << M;

	return 0;
}