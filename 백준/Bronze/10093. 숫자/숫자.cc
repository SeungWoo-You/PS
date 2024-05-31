#include <iostream>
#include <algorithm>

using namespace std;

int main() {
	long long A, B;
	long long m, M;

	cin >> A >> B;

	M = max(A, B);
	m = min(A, B);

	if (M == m) printf("%lld\n", M - m);
	else printf("%lld\n", M - m - 1);

	for (long long i = m + 1; i < M; i++) printf("%lld ", i);

	return 0;
}