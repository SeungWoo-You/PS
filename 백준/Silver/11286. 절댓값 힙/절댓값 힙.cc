#include <iostream>
#include <queue>
#include <cstdlib>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int N;
	cin >> N;

	priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> PQ;

	while (N--) {
		int x;
		cin >> x;

		if (x == 0) {
			if (PQ.empty()) cout << 0 << '\n';
			else {
				pair<int, int> elem = PQ.top();
				cout << elem.second << '\n';
				PQ.pop();
			}
		}
		else PQ.push({abs(x), x});
	}

	return 0;
}
