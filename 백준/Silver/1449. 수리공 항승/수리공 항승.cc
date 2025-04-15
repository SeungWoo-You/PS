#include <iostream>

using namespace std;

int sinks[1000];
int temp_sinks[1000];

int get_max(int N) {
	int max = sinks[0];

	for (int i = 1; i < N; i++) {
		if (sinks[i] > max)
			max = sinks[i];
	}

	return max;
}

void counting_sort(int N, int place) {
	int counts[10] = {0};

	for (int i = 0; i < N; i++) {
		int idx = (sinks[i] / place) % 10;
		counts[idx]++;
	}

	for (int i = 1; i < 10; i++)
		counts[i] += counts[i - 1];

	for (int i = N - 1; i >= 0; i--) {
		int idx = (sinks[i] / place) % 10;
		temp_sinks[counts[idx] - 1] = sinks[i];
		counts[idx]--;
	}

	for (int i = 0; i < N; i++)
		sinks[i] = temp_sinks[i];
}

void radix_sort(int N) {
	int max_elem = get_max(N);

	for (int place = 1; max_elem / place > 0; place *= 10)
		counting_sort(N, place);
}


int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	int N, L;

	cin >> N >> L;
	for (int i = 0; i < N; i++)
		cin >> sinks[i];

	radix_sort(N);

	int count = 1, taped = sinks[0];

	for (int i = 1; i < N; i++) {
		if (sinks[i] - taped >= L) {
			count++;
			taped = sinks[i];
		}
	}

	cout << count;

	return 0;
}