#include <iostream>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	int x, y;
	cin >> x >> y;
	
	int answer = 1;

	while (x || y) {
		if (x % 3 + y % 3 != 1) {
			answer = 0;
			break;
		}

		x /= 3, y /= 3;
	}

	cout << answer;

	return 0;
}