#include <iostream>
#include <stack>

using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	int N;
	stack<int> stk;

	cin >> N;

	while (N--) {
		int cmd;
		cin >> cmd;

		if (cmd == 1) {
			int num;
			cin >> num;

			stk.push(num);
		}
		else if (cmd == 2) {
			if (stk.empty()) cout << -1 << '\n';
			else {
				cout << stk.top() << '\n';
				stk.pop();
			}
		}
		else if (cmd == 3) cout << stk.size() << '\n';
		else if (cmd == 4) {
			if (stk.empty()) cout << 1 << '\n';
			else cout << 0 << '\n';
		}
		else if (cmd == 5) {
			if (stk.empty()) cout << -1 << '\n';
			else cout << stk.top() << '\n';
		}
	}

	return 0;
}