#include <iostream>
#define MAX_N 50
#define MAX_M 50

using namespace std;

int boxes[MAX_N] = {0};
int books[MAX_M] = {0};

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	int N, M;
	cin >> N >> M;

	for (int i = 0; i < N; i++)
		cin >> boxes[i];
	for (int i = 0; i < M; i++)
		cin >> books[i];

	int unused = 0;
	int xid = 0;

	for (int j = 0; j < M;) {
		if (books[j] <= boxes[xid])
			boxes[xid] -= books[j++];
		else
			unused += boxes[xid++];
	}

	for (int i = xid; i < N; i++)
		unused += boxes[i];

	cout << unused;

	return 0;
}