#include <iostream>

using namespace std;

char words[10][9];
int counts[26] = {0};

int make_key(char a) {
	return a - 'A';
}

void swap(int* a, int* b) {
	int temp = *a;
	*a = *b;
	*b = temp;
}

int get_pivot(int left, int right) {
	int k = left;
	
	for (int i = left + 1; i <= right; i++) {
		if (counts[i] > counts[left]) swap(counts[++k], counts[i]);
	}

	swap(counts[k], counts[left]);

	return k;
}

void quick_sort(int left, int right) {
	if (left < right) {
		int pivot = get_pivot(left, right);
		quick_sort(left, pivot);
		quick_sort(pivot + 1, right);
	}
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	int N;
	cin >> N;

	for (int i = 0; i < N; i++) {
		cin >> words[i];

		int size = 0;

		for (int j = 0; words[i][j] != '\0'; j++) size++;

		for (int j = size - 1, e = 1; j >= 0; j--, e *= 10)
			counts[make_key(words[i][j])] += e;
	}

	quick_sort(0, 25);

	int answer = 0;

	for (int c = 0, n = 9; counts[c] > 0; c++, n--)
		answer += counts[c] * n;

	cout << answer;

	return 0;
}