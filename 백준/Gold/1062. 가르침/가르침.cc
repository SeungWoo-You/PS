#include <iostream>

#define MAX_N 50

using namespace std;

int selected = 0;
int N, K;
int words[50] = {0};
int answer = 0;

void teach(int cid, int used) {
	if (used == K) {
		int res = 0;

		for (int wid = 0; wid < N; wid++)
			if ((selected & words[wid]) == words[wid]) res++;

		if (answer < res) answer = res;

		return;
	}

	for (int i = cid; i <= 26; i++) {
		if (selected & (1 << i)) continue;

		selected |= (1 << i);
		teach(i, used + 1);
		selected &= ~(1 << i);
	}
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	cin >> N >> K;

	if (K < 5) {
		cout << 0;
		return 0;
	}

	char word[16] = "antic";

	for (int w = 0; word[w] != 0; w++)
		selected |= 1 << (word[w] - 'a');

	for (int i = 0; i < N; i++) {
		cin >> word;

		for (int w = 0; word[w] != 0; w++)
			words[i] |= 1 << (word[w] - 'a');
	}

	teach(0, 5);

	cout << answer;

	return 0;
}