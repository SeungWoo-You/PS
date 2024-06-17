#include <iostream>
#include <queue>
#include <array>

#define INF (~0U >> 2)
#define MAX 200001

using namespace std;

array<int, MAX> checked = {0};

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int N, K;
	cin >> N >> K;

	int time = INF, path = 0;
	queue<pair<int, int>> Q;
	Q.push({N, 0});
	checked.fill(INF);

	while (!Q.empty()) {
		int u = Q.front().first, w = Q.front().second;
		Q.pop();

		if (w > time) break;

		if (u == K) {
			if (w < time) {
				time = w;
				path = 1;
			}
			else if (w == time) path++;
		}
		
		if (u - 1 >= 0 && checked[u - 1] >= w + 1) {
			checked[u - 1] = w + 1;
			Q.push({u - 1, w + 1});
		}
		if (u + 1 < MAX && checked[u + 1] >= w + 1) {
			checked[u + 1] = w + 1;
			Q.push({u + 1, w + 1});
		}
		if (2 * u < MAX && checked[2 * u] >= w + 1) {
			checked[2 * u] = w + 1;
			Q.push({2 * u, w + 1});
		}
		
	}

	cout << time << '\n';
	cout << path;

	return 0;
}