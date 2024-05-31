#include <iostream>
#include <algorithm>
#include <queue>

using namespace std;

int main() {
	const int N = 10;
	int M = 0, current = 0;
	queue<pair<int, int>> Q;

	for (int i = 0; i < N; i++) {
		int people_in, people_out;

		cin >> people_out >> people_in;
		Q.push({ people_out, people_in });
	}

	while (!Q.empty()) {
		pair<int, int> info = Q.front();
		int people_in = info.second, people_out = info.first;
		Q.pop();

		current += people_in - people_out;
		M = max(M, current);
	}

	printf("%d", M);

	return 0;
}