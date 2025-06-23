#include <iostream>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	int X, N;
	cin >> X >> N;

	int total = 0;

	for (int i = 0; i < N; i++) {
		int a, b;
		cin >> a >> b;

		total += a * b;
	}

	cout << (total == X ? "Yes" : "No");

	return 0;
}