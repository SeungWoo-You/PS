#include <iostream>

#define MAX_S 100

using namespace std;

char S[MAX_S + 1] = {0};
char num[MAX_S + 1] = {0};

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	cin >> S;

	int size = 0;
	int sum = 0;

	for (int i = 0; S[i] != 0; i++) {
		if (S[i] != ',') num[size++] = S[i] - '0';
		else {
			for (int i = size - 1, exp = 1; i >= 0; i--, exp *= 10)
				sum += num[i] * exp;

			size = 0;
		}
	}

	for (int i = size - 1, exp = 1; i >= 0; i--, exp *= 10)
		sum += num[i] * exp;

	cout << sum;

	return 0;
}