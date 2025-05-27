#include <iostream>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	int N;
	cin >> N;

	while (N--) {
		long long key;
		cin >> key;

		bool flag = true;

		for (int i = 2; i <= 1'000'000; i++)
			if (key % i == 0) {
				flag = false;
				break;
			}

		cout << (flag ? "YES\n" : "NO\n");
	}

	return 0;
}