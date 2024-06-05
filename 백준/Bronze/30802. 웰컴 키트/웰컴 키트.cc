#include <iostream>
#include <array>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int N, T, P;
	array<int, 6> sizes;

	cin >> N;
	for (int i = 0; i < 6; i++) {
		cin >> sizes[i];
	}
	cin >> T >> P;

	int t_total = 0;
	
	for (int x : sizes) {
		int quot = x / T, rem = x % T;
		
		t_total += quot;
		if (rem) t_total += 1;
	}

	cout << t_total << '\n';
	cout << N / P << ' ' << N % P;

	return 0;
}