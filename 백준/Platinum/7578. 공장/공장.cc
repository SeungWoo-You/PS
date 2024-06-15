#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

typedef long long LLT;

void update(vector<int>* T, int N, int i) {
	for ((*T)[i += N] = 1; i > 1; i >>= 1)
		(*T)[i >> 1] = (*T)[i] + (*T)[i ^ 1];
}

LLT query(vector<int>* T, int N, int l, int r) {
	LLT result = 0;

	for (l += N, r += N; l < r; l >>= 1, r >>= 1) {
		if (l % 2) result += (*T)[l++];
		if (r % 2) result += (*T)[--r];
	}

	return result;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int N;
	cin >> N;

	vector<int> A(N);
	for (int i = 0; i < N; i++) cin >> A[i];

	unordered_map<int, int> B;
	for (int i = 0; i < N; i++) {
		int x;
		cin >> x;

		B[x] = i;
	}

	vector<int> T(2 * N);
	LLT answer = 0;

	for (int a : A) {
		answer += query(&T, N, B[a], N);
		update(&T, N, B[a]);
	}

	cout << answer;

	return 0;
}