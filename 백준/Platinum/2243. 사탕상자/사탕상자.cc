#include <iostream>
#include <vector>

#define SIZE 1000001

using namespace std;

typedef long long LLT;

void update(vector<LLT>* T, int node, int start, int end, int i, LLT val) {
	if (i < start || i > end) return;
	if (start == end) {
		(*T)[node] = val;
		return;
	}

	int mid = (start + end) / 2;
	update(T, node << 1, start, mid, i, val);
	update(T, node << 1 | 1, mid + 1, end, i, val);
	(*T)[node] = (*T)[node << 1] + (*T)[node << 1 | 1];

	return;
}

int query(vector<LLT>* T, int node, int start, int end, LLT k) {
	if (start == end) return end;

	int mid = (start + end) / 2;
	if ((*T)[node << 1] >= k)
		return query(T, node << 1, start, mid, k);
	else
		return query(T, node << 1 | 1, mid + 1, end, k - (*T)[node << 1]);
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int N;
	cin >> N;

	vector<LLT> box(SIZE, 0), T(4 * SIZE, 0);

	while (N--) {
		int A, B;
		cin >> A >> B;

		if (A == 1) {
			int rank = query(&T, 1, 1, SIZE, (LLT) B);
			cout << rank << '\n';
			update(&T, 1, 1, SIZE, rank, box[rank] - 1);
			box[rank]--;
		}
		else if (A == 2) {
			LLT C;
			cin >> C;

			update(&T, 1, 1, SIZE, B, box[B] + C);
			box[B] += C;
		}
	}

	return 0;
}