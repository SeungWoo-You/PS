#include <iostream>

#define MAX_G 100'000

using namespace std;

int results[MAX_G] = {0};
int res_size = 0;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	int G;
	cin >> G;

	int x = 1, y = 1;

	while (true) {
		long long diff = ((long long) x) * x - ((long long) y) * y;

		if (diff > G && x - y == 1) break;

		if (diff == G) results[res_size++] = x;
		if (diff <= G) x++;
		else y++;
	}

	if (res_size == 0) cout << -1;
	else
		for (int i = 0; i < res_size; i++)
			cout << results[i] << '\n';

	return 0;
}