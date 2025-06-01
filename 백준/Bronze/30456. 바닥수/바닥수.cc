#include <iostream>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	int N, L;
	cin >> N >> L;

	for (int i = 1; i < L; i++) cout << 1;
	cout << N;

	return 0;
}