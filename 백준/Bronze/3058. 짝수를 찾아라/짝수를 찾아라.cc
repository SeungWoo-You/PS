#include <iostream>
#include <algorithm>

using namespace std;

int main() {
	int T;

	cin >> T;

	while (T--) {
		int nums[7], total = 0, min_value = 100;

		for (int i = 0; i < 7; i++) cin >> nums[i];

		for (int x : nums) {
			if (!(x & 1)) {
				total += x;
				min_value = min(min_value, x);
			}
		}
		printf("%d %d\n", total, min_value);
	}

	return 0;
}