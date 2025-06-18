#include <iostream>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	int a, b, c, d, e, f;

	cin >> a >> b >> c >> d >> e >> f;

	cout << (c * e - b * f) / (a * e - b * d) << ' '
		<< (a * f - c * d) / (a * e - b * d);

	return 0;
}