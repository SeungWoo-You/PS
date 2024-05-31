#include <iostream>
#include <algorithm>

using namespace std;

int main() {
	int A, B;
	int m, M;

	cin >> A >> B;

	M = max(A, B);
	m = min(A, B);

	if (M == m) printf("%d\n", M - m);
	else printf("%d\n", M - m - 1);

	for (int i = m + 1; i < M; i++) printf("%d ", i);

	return 0;
}