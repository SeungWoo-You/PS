#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
	int n, x, total = 0;

	cin >> n;

	vector<int> nums(n);

	for (int i = 0; i < n; i++) cin >> nums[i];
	cin >> x;

	sort(nums.begin(), nums.end());

	for (int i = 0; i < n; i++) {
		int start = i + 1, end = n - 1;
		int target = x - nums[i];

		if (target <= 0) break;

		while (start <= end) {
			int mid = (start + end) / 2;

			if (nums[mid] < target) start = mid + 1;
			else if (nums[mid] > target) end = mid - 1;
			else {
				total += 1;
				break;
			}
		}
	}
	printf("%d", total);
}