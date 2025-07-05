#include <iostream>

#define COIN_N 40

using namespace std;

char coins[COIN_N + 1] = {0};

void coins_to_binary() {
	for (int i = 0; i < COIN_N; i++)
		coins[i] = coins[i] == 'H';
}

int get_key(char arr[]) {
	return arr[0] * 4 + arr[1] * 2 + arr[2];
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	int P;
	cin >> P;

	while (P--) {
		cin >> coins;
		coins_to_binary();
		int counts[8] = {0};

		for (int i = 0; i < COIN_N - 2; i++)
			counts[get_key(coins + i)]++;
		for (int i = 0; i < 8; i++)
			cout << counts[i] << ' ';

		cout << '\n';
	}

	return 0;
}