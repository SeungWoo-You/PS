#include <iostream>

using namespace std;

#define SIZE 64

bool visited[SIZE][SIZE] = {false};
int N, val;


int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	cin >> N;
	visited[0][0] = true;

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			cin >> val;

			if (!visited[i][j]) continue;
			if (i + val < N) visited[i + val][j] = true;
			if (j + val < N) visited[i][j + val] = true;
		}
	}

	cout << (visited[N - 1][N - 1] ? "HaruHaru" : "Hing");

	return 0;
}