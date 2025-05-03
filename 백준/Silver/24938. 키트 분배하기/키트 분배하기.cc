#include <iostream>

#define MAX_N 200'000
#define ABS(x) ((x) > 0 ? (x) : -(x))

using namespace std;

int rooms[MAX_N];

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	int N;
	cin >> N;

	long long total = 0;

	for (int i = 0; i < N; i++) {
		cin >> rooms[i];
		total += rooms[i];
	}

	long long K = total / N;
	long long count = 0, kit = 0;

	for (int i = 0; i < N; i++) {
		kit += rooms[i] - K;
		count += ABS(kit);
	}

	cout << count;

	return 0;
}