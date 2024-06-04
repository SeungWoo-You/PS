#include <iostream>
#include <queue>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int N;
	cin >> N;

	queue<int> Q;

	int cmd;
	cin >> cmd;

	while (cmd != -1) {
		if (cmd == 0) Q.pop();
		else {
			if (Q.size() < N) Q.emplace(cmd);
		}

		cin >> cmd;
	}

	if (Q.empty()) cout << "empty";
	else {
		while (!Q.empty()) {
			int c = Q.front();
			Q.pop();
			cout << c << ' ';
		}
	}

	return 0;
}