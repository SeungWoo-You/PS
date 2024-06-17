#include <iostream>
#include <array>

using namespace std;

typedef long long LLT;

void add(array<LLT, 10>* nums, int x, LLT digit) {
	while (x > 0) {
		(*nums)[x % 10] += digit;
		x /= 10;
	}
	
	return;
}

void count_pages(array<LLT, 10>* nums, int l, int r, LLT digit) {
	while (l % 10 != 0 && l <= r) add(nums, l++, digit);

	if (l > r) return;

	while (r % 10 != 9 && l <= r) add(nums, r--, digit);

	int c = r / 10 - l / 10 + 1;
	for (int i = 0; i < 10; i++) (*nums)[i] += c * digit;

	return count_pages(nums, l / 10, r / 10, digit * 10);
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int N;
	cin >> N;
	
	array<LLT, 10> nums = {0};

	count_pages(&nums, 1, N, 1);

	for (auto x : nums) cout << x << ' ';

	return 0;
}