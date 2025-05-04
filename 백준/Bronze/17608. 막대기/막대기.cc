#include <iostream>

#define MAX_N 100'000

using namespace std;

int arr[MAX_N] = {0};

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	int N;
	cin >> N;

	int idx = -1;

	for (int i = 0; i < N; i++) {
		int x;
		cin >> x;

		while (idx >= 0 && arr[idx] <= x) idx--;
		
		arr[++idx] = x;
	}

	cout << idx + 1;

	return 0;
}