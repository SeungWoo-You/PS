#include <iostream>

#define MAX_CASE 2000
#define MAX_M 8
#define MAX_N 8

using namespace std;

int combs[MAX_CASE][MAX_M] = {0};
int combs_size = 0;
int nums[MAX_N] = {0};
int temps[MAX_N] = {0};

void generate_combs(int n, int r, int len, int start, int temp[MAX_M]) {
	if (len == r) {
		for (int i = 0; i < r; i++) combs[combs_size][i] = temp[i];
		combs_size++;

		return;
	}

	for (int i = start; i < n; i++) {
		temp[len] = nums[i];
		generate_combs(n, r, len + 1, i + 1, temp);
	}
}

void merge(int left, int mid, int right) {
	int i = left, j = mid + 1, k = left;

	while (i <= mid && j <= right) {
		if (nums[i] < nums[j]) temps[k++] = nums[i++];
		else temps[k++] = nums[j++];
	}

	while (i <= mid) temps[k++] = nums[i++];
	while (j <= right) temps[k++] = nums[j++];

	for (int t = left; t <= right; t++) nums[t] = temps[t];
}

void merge_sort(int left, int right) {
	if (left < right) {
		int mid = (left + right) >> 1;
		merge_sort(left, mid);
		merge_sort(mid + 1, right);
		merge(left, mid, right);
	}
}


int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	int N, M;
	cin >> N >> M;

	for (int i = 0; i < N; i++) cin >> nums[i];

	merge_sort(0, N - 1);
	generate_combs(N, M, 0, 0, temps);

	for (int i = 0; i < combs_size; i++) {
		for (int j = 0; j < M; j++) cout << combs[i][j] << ' ';
		cout << '\n';
	}

	return 0;
}