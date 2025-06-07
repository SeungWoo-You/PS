#include <iostream>

#define MAX_N 200'000
#define MAX_X 1'000'000'000

using namespace std;

int houses[MAX_N], temps[MAX_N];

void merge(int left, int mid, int right) {
	int i = left, j = mid + 1, k = left;

	while (i <= mid && j <= right) {
		if (houses[i] <= houses[j]) temps[k++] = houses[i++];
		else temps[k++] = houses[j++];
	}

	while (i <= mid) temps[k++] = houses[i++];
	while (j <= right) temps[k++] = houses[j++];

	for (int t = left; t <= right; t++)
		houses[t] = temps[t];
}

void merge_sort(int left, int right) {
	if (left < right) {
		int mid = (left + right) >> 1;
		merge_sort(left, mid);
		merge_sort(mid + 1, right);
		merge(left, mid, right);
	}
}

int place_wifis(int N, int C) {
	int left = 0, right = MAX_X;
	int res = -1;

	while (left <= right) {
		int mid = (left + right) >> 1;
		int count = 1;
		int prev_house = houses[0];

		for (int i = 1; i < N; i++)
			if (houses[i] - prev_house >= mid)
				count++, prev_house = houses[i];

		if (count >= C) left = mid + 1, res = mid;
		else right = mid - 1;
	}

	return res;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	int N, C;
	cin >> N >> C;

	for (int i = 0; i < N; i++)
		cin >> houses[i];

	merge_sort(0, N - 1);

	cout << place_wifis(N, C);

	return 0;
}