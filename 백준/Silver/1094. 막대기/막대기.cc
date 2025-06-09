#include <iostream>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	int X;
	cin >> X;

	int count = 0;
	while (X > 0) {
		X &= (X - 1);
		count++;
	}

	cout << count;

	return 0;
}