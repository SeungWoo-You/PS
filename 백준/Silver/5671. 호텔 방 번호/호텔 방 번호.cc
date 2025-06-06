#include <iostream>

#define MAX_M 5001

using namespace std;

int counts[MAX_M] = {0};

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	for (int i = 1; i < MAX_M; i++) {
		bool checked[10] = {false};
		int num = i;
		
		while (num) {
			if (checked[num % 10]) break;
			checked[num % 10] = true;
			num /= 10;
		}
		counts[i] = counts[i - 1] + (num > 0 ? 0 : 1);
	}

	while (true) {
		int N, M;
		cin >> N >> M;
		
		if (cin.eof()) break;

		cout << counts[M] - counts[N - 1] << '\n';
	}

	return 0;
}