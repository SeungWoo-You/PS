#include <iostream>

#define MAX_N 10

using namespace std;

char nums[6 * MAX_N + 1];
char code_map[8][7];
char secrets[8] = {
	0b000000,
	0b001111,
	0b010011,
	0b011100,
	0b100110,
	0b101001,
	0b110101,
	0b111010
};

void init() {
	for (int c = 0; c < 8; c++)
		code_map[c][0] = secrets[c];

	for (int c = 0; c < 8; c++)
		for (int i = 1, base = 1; i < 7; i++, base <<= 1)
			code_map[c][i] = code_map[c][0] ^ base;
}

char get_code(const char num[]) {
	int res = 0;
	
	for (int i = 5, base = 1; i >= 0; i--, base <<= 1)
		res += (num[i] - '0') * base;

	return res;
}

char decode(char code) {
	for (int c = 0; c < 8; c++)
		for (int i = 0; i < 7; i++)
			if (code_map[c][i] == code) return c + 'A';
	return 0;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	init();

	int N;
	cin >> N >> nums;

	char res[MAX_N] = {0};

	for (int i = 0; i < N; i++) {
		char code = get_code(&nums[6 * i]);
		char alpha = decode(code);
		
		if (alpha == 0) {
			cout << i + 1;
			return 0;
		}

		res[i] = alpha;
	}

	cout << res;

	return 0;
}