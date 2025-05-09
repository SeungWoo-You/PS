#include <iostream>

using namespace std;

int num_sizes[10] = {1, 1, 4, 4, 2, 1, 1, 4, 4, 2};
int coms[10][4] = {
	{10, -1, -1, -1},
	{1, -1, -1, -1},
	{6, 2, 4, 8},
	{1, 3, 9, 7},
	{6, 4, -1, -1},
	{5, -1, -1, -1},
	{6, -1, -1, -1},
	{1, 7, 9, 3},
	{6, 8, 4, 2},
	{1, 9, -1, -1}
};

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	int T;
	cin >> T;

	while (T--) {
		int a, b;
		cin >> a >> b;

		int c = a % 10;
		int n = b % num_sizes[c];

		cout << coms[c][n] << '\n';
	}

	return 0;
}