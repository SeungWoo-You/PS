#include <iostream>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	int N, K;
	cin >> N >> K;

	int pivot, x, count = 0, day = 0;
	cin >> pivot;

	for (int i = 1; i < N; i++) {
		cin >> x;
		
		if (x == pivot) continue;

		count += x - pivot;
		day++;
	}

	cout << count << ' ' << day;

	return 0;
}