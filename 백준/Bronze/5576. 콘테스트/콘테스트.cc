#include <iostream>
#include <array>
#include <algorithm>
#include <numeric>

#define SIZE 10

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	array<int, SIZE> W, K;
	for (int i = 0; i < SIZE; i++) cin >> W[i];
	for (int i = 0; i < SIZE; i++) cin >> K[i];

	sort(W.begin(), W.end());
	sort(K.begin(), K.end());

	cout << accumulate(W.end() - 3, W.end(), 0) << '\n';
	cout << accumulate(K.end() - 3, K.end(), 0);

	return 0;
}