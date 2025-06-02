#include <iostream>

#define KEY_LEN 10
#define SECRET_LEN 100

using namespace std;

int temp_code[KEY_LEN + 1];

void counting_sort(int key[], int code[], int N, int exp) {
	int counts[10] = {0};

	for (int i = 0; i < N; i++) {
		int kid = code[i];
		int idx = (key[kid] / exp) % 10;
		counts[idx]++;
	}

	for (int i = 1; i < 10; i++)
		counts[i] += counts[i - 1];

	for (int i = N - 1; i >= 0; i--) {
		int kid = code[i];
		int idx = (key[kid] / exp) % 10;
		temp_code[--counts[idx]] = code[i];
	}

	for (int i = 0; i < N; i++)
		code[i] = temp_code[i];
}

void radix_sort(int key[], int code[], int N) {
	int max_elem = 0;

	for (int i = 0; i < N; i++)
		if (max_elem < key[i]) max_elem = key[i];

	for (int exp = 1; max_elem / exp > 0; exp *= 10)
		counting_sort(key, code, N, exp);
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	char key[KEY_LEN + 1] = {0}, secret[SECRET_LEN + 1] = {0};
	int key_int[KEY_LEN + 1] = {0};
	int code[KEY_LEN] = {0}, decode[KEY_LEN] = {0};
	int key_len = 0, chunks = 0;

	cin >> key >> secret;

	for (; key[key_len] != 0; key_len++) {
		code[key_len] = decode[key_len] = key_len;
		key_int[key_len] = key[key_len];
	}

	radix_sort(key_int, code, key_len);
	radix_sort(code, decode, key_len);

	for (; secret[chunks * key_len] != 0; chunks++);

	int i = 0, j = 0;

	while (i < chunks && j < key_len) {
		cout << secret[decode[j] * chunks + i];
		j++;

		if (j == key_len) j = 0, i++;
	}

	return 0;
}