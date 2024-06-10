#include <iostream>
#include <array>
#include <unordered_map>
#include <queue>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int N, M;
	cin >> N >> M;

	unordered_map<int, int> ladders, snakes;
	for (int i = 0; i < N; i++) {
		int src, dst;
		cin >> src >> dst;
		ladders[src] = dst;
	}
	for (int i = 0; i < M; i++) {
		int src, dst;
		cin >> src >> dst;
		snakes[src] = dst;
	}

	array<int, 101> board = {0};
	array<int, 6> dice = {1, 2, 3, 4, 5, 6};
	queue<int> Q;
	Q.push(1);

	while (!Q.empty()) {
		int idx = Q.front();
		Q.pop();
		
		if (board[100] != 0) break;
		
		for (int dx : dice) {
			int x = idx + dx;

			if (x > 100) continue;

			if (ladders.count(x)) x = ladders[x];
			else if (snakes.count(x)) x = snakes[x];

			if (board[x] == 0) {
				Q.push(x);
				board[x] = board[idx] + 1;
			}
		}
	}

	cout << board[100];

	return 0;
}