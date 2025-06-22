#include <iostream>

using namespace std;

int sums[81] = {0};

int make_key(int s1, int s2, int s3) {
	return s1 + s2 + s3;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	int S1, S2, S3;
	cin >> S1 >> S2 >> S3;

	for (int i = 1; i <= S1; i++)
		for (int j = 1; j <= S2; j++)
			for (int k = 1; k <= S3; k++)
				sums[make_key(i, j, k)]++;

	int max = 0, res = -1;

	for (int i = 3; i <= 80; i++)
		if (max < sums[i]) max = sums[i], res = i;

	cout << res;

	return 0;
}