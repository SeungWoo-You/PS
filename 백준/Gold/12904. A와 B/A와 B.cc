#include <iostream>

using namespace std;

bool compare(char S[], char T[], int size, int t_start, int t_end, bool reversed) {
	if (reversed) {
		for (int i = 0; i < size; i++)
			if (S[i] != T[t_end - i]) return false;
	}
	else {
		for (int i = 0; i < size; i++)
			if (S[i] != T[t_start + i]) return false;
	}

	return true;
}

int main() {
	ios_base::sync_with_stdio(false);

	char S[1000] = {0}, T[1001] = {0};
	int S_size = 0, T_size = 0;

	cin >> S >> T;

	while (S[S_size] != 0) S_size++;
	while (T[T_size] != 0) T_size++;

	int left = 0, right = T_size - 1;
	bool reversed = false;

	while (right - left + 1 != S_size) {
		if (reversed) {
			if (T[left] == 'B') reversed = false;

			left++;
		}
		else {
			if (T[right] == 'B') reversed = true;

			right--;
		}
	}

	cout << (int) compare(S, T, S_size, left, right, reversed);

	return 0;
}