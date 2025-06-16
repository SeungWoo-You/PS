#include <iostream>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	int N, K;
	
	while (cin >> N >> K) {
		int total = 0;
		int coupon = N;
		int stamp = 0;

		while (coupon > 0) {
			total += coupon;
			stamp += coupon;
			coupon = stamp / K;
			stamp -= stamp / K * K;
		}

		cout << total << '\n';
	}

	return 0;
}