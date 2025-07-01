#include <iostream>

#define MAX_C 4000

using namespace std;

bool checked[MAX_C] = {false};

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	int N, L, D;
	cin >> N >> L >> D;

	int idx = 0;

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < L; j++)
			checked[idx++] = true;
		for (int t = 0; t < 5; t++) idx++;
	}

	for (int i = 0; i < MAX_C; i += D)
		if (!checked[i]) {
			cout << i;
			break;
		}

	return 0;
}