#include <iostream>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	int A, B, C, D, E;
	cin >> A >> B >> C >> D >> E;

	int time = 0;

	if (A < 0) {
		if (B < 0) time = (B - A) * C;
		else if (B == 0) time = (B - A) * C + D;
		else time = (-A) * C + D + B * E;
	}
	else time = (B - A) * E;

	cout << time;

	return 0;
}