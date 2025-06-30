#include <iostream>

#define MAX_COMB 252
#define MAX_VIRUS 10
#define MAX_N 50
#define INF (~0U >> 2)

using namespace std;

struct Point {
	int x, y;
};

struct QData {
	int x, y, depth;
};

class Queue {
private:
	const static int ARR_SIZE = MAX_N * MAX_N;
	QData arr[ARR_SIZE];
	int arr_size = 0;
	int front = 0;
	int rear = -1;

public:
	void init() {
		arr_size = 0;
		front = 0;
		rear = -1;
	}

	void push(QData X) {
		rear = (rear + 1) % ARR_SIZE;
		arr[rear] = X;
		arr_size++;
	}

	QData pop() {
		QData* data = &arr[front];
		front = (front + 1) % ARR_SIZE;
		arr_size--;

		return *data;
	}

	int size() {
		return arr_size;
	}

	bool empty() {
		return arr_size == 0;
	}
};

Point combs[MAX_COMB][MAX_VIRUS] = {0};
int comb_count = 0;
Point possible_pos[MAX_VIRUS];
int pos_count = 0;
int board[MAX_N][MAX_N] = {0};
int visited[MAX_N][MAX_N] = {0};
int vgen = 0;
int Dx[4] = {0, 0, -1, 1};
int Dy[4] = {-1, 1, 0, 0};
Queue Q;
int N, M;

void generate_combinations(int n, int r, int start, int depth, Point comb[]) {
	if (depth == r) {
		for (int i = 0; i < r; i++)
			combs[comb_count][i] = comb[i];
		comb_count++;
		return;
	}

	for (int i = start; i < n; i++) {
		comb[depth] = possible_pos[i];
		generate_combinations(n, r, i + 1, depth + 1, comb);
	}
}

int spread(Point starts[MAX_VIRUS], int size) {
	int result = 0;
	vgen++;
	Q.init();

	for (int i = 0; i < size; i++) {
		Q.push({starts[i].x, starts[i].y, 0});
		visited[starts[i].x][starts[i].y] = vgen;
	}

	while (!Q.empty()) {
		QData data = Q.pop();

		for (int d = 0; d < 4; d++) {
			int x = data.x + Dx[d], y = data.y + Dy[d];

			if (0 <= x && x < N && 0 <= y && y < N && visited[x][y] != vgen && board[x][y] != 1) {
				int depth = data.depth + 1;

				if (result < depth) result = depth;

				visited[x][y] = vgen;
				Q.push({x, y, depth});
			}
		}
	}

	for (int i = 0; i < N; i++)
		for (int j = 0; j < N; j++)
			if (board[i][j] != 1 && visited[i][j] != vgen)
				return -1;

	return result;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	cin >> N >> M;

	for (int i = 0; i < N; i++)
		for (int j = 0; j < N; j++) {
			cin >> board[i][j];

			if (board[i][j] == 2) possible_pos[pos_count++] = {i, j};
		}

	Point temps[MAX_VIRUS];
	int result = INF;

	generate_combinations(pos_count, M, 0, 0, temps);

	for (int i = 0; i < comb_count; i++) {
		int temp_res = spread(combs[i], M);

		if (temp_res != -1 && result > temp_res) result = temp_res;
	}

	cout << (result == INF ? -1 : result);

	return 0;
}