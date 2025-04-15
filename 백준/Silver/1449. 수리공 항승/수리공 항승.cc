#include <iostream>

using namespace std;

bool sinks[1001];

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	int N, L;

	cin >> N >> L;
	for (int i = 0, s; i < N; i++) {
		cin >> s;
		sinks[s] = true;
	}

	int count = 0;

	for (int i = 0; i <= 1000; i++) {
		if (sinks[i]) {
			count++;
			i += L - 1;
		}
	}

	cout << count;

	return 0;
}