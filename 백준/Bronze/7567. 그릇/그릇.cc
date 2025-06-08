#include <iostream>

#define MAX_N 51

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	char dishes[MAX_N] = {0};
	cin >> dishes;

	bool is_up = dishes[0] == '(';
	int height = 10;

	for (int i = 1; dishes[i] != 0; i++) {
		if (dishes[i] == '(')
			height += is_up ? 5 : 10;
		else
			height += is_up ? 10 : 5;

		is_up = dishes[i] == '(';
	}

	cout << height;

	return 0;
}