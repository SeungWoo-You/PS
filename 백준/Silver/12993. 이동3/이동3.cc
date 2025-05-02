#include <iostream>

#define MAX(x, y) ((x) > (y) ? (x) : (y))

using namespace std;

int steps[20];

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	int x, y;
	cin >> x >> y;
	
	if (x == 0 && y == 0) {
		cout << 1;

		return 0;
	}

	int limits = 0;
	steps[0] = 1;

	for (int i = 1; i < 20; i++) {
		steps[i] = steps[i - 1] * 3;
		
		if (steps[i] > MAX(x, y)) {
			limits = i - 1;
			break;
		}
	}

	for (int p = limits; p >= 0; p--) {
		if (x > y) x -= steps[p];
		else y -= steps[p];
	}

	cout << (int) (x == 0 && y == 0);

	return 0;
}