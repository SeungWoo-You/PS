#include <iostream>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	int N;
	cin >> N;

	cout << N * 78 / 100 << ' ';
	cout << (N * 80 / 100) + (N * 20 / 100 * 78 / 100);
	return 0;
}