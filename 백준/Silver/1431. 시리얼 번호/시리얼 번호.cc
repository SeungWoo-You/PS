#include <iostream>

#define MAX_N 50
#define MAX_LEN 50

char serials[MAX_N][MAX_LEN + 1] = {0};
int lengths[MAX_N] = {0};
int len_temps[MAX_N] = {0};
int seri_idx[MAX_N] = {0};
int seri_temps[MAX_N] = {0};

using namespace std;

// A가 더 작으면 -, 크면 +
int compare(char A[], int A_len, char B[], int B_len) {
	if (A_len == B_len) {
		int A_sum = 0, B_sum = 0;

		for (int i = 0; i < A_len; i++) {
			int a = A[i] - '0', b = B[i] - '0';

			if (0 <= a && a <= 9) A_sum += a;
			if (0 <= b && b <= 9) B_sum += b;
		}

		if (A_sum == B_sum) {
			for (int i = 0; i < A_len; i++)
				if (A[i] != B[i]) return A[i] - B[i];

			return 0;
		}
		else return A_sum - B_sum;
	}
	else return A_len - B_len;
}

void merge(int left, int mid, int right) {
	int i = left, j = mid + 1, k = left;

	while (i <= mid && j <= right) {
		if (compare(serials[seri_idx[i]], lengths[i], serials[seri_idx[j]], lengths[j]) < 0)
			len_temps[k] = lengths[i], seri_temps[k++] = seri_idx[i++];
		else len_temps[k] = lengths[j], seri_temps[k++] = seri_idx[j++];
	}

	while (i <= mid) len_temps[k] = lengths[i], seri_temps[k++] = seri_idx[i++];
	while (j <= right) len_temps[k] = lengths[j], seri_temps[k++] = seri_idx[j++];

	for (int t = left; t <= right; t++)
		lengths[t] = len_temps[t], seri_idx[t] = seri_temps[t];
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

	int N;
	cin >> N;

	for (int i = 0; i < N; i++) {
		cin >> serials[i];
		seri_idx[i] = i;

		for (int j = 0; serials[i][j] != 0; j++) lengths[i]++;
	}

	merge_sort(0, N - 1);

	for (int i = 0; i < N; i++)
		cout << serials[seri_idx[i]] << '\n';

	return 0;
}