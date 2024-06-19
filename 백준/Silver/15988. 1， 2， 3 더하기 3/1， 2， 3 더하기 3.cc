#include <iostream>
#include <array>

#define SIZE 1000001
#define DIV 1000000009

using namespace std;

array<int, SIZE> nums = {0};

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int T;
	cin >> T;

	nums[1] = 1, nums[2] = 2, nums[3] = 4;
	int end = 3;

	while (T--) {
		int N;
		cin >> N;

		if (end >= N) {
			cout << nums[N] << '\n';
			continue;
		}

		for (; end < N; end++)
			nums[end + 1] = ((nums[end] + nums[end - 1]) % DIV + nums[end - 2]) % DIV;
		
		cout << nums[N] << '\n';
	}

	return 0;
}