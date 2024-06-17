#include <iostream>
#include <stack>
#include <unordered_map>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	string formula;
	cin >> formula;

	stack<char> S;
	unordered_map<char, int> opers = {
		{'+', 1},
		{'-', 1},
		{'*', 2},
		{'/', 2}
	};

	for (char x : formula) {
		if (x == ')') {
			while (S.top() != '(') {
				cout << S.top();
				S.pop();
			}
			S.pop();
		}
		else if (x == '(' || !opers.count(x)) S.push(x);
		else {
			while (!S.empty() && S.top() != '(') {
				char t = S.top();

				if (!opers.count(t) || opers[t] >= opers[x]) {
					cout << t;
					S.pop();
				}
				else break;
			}
			S.push(x);
		}
	}

	while (!S.empty()) {
		cout << S.top();
		S.pop();
	}

	return 0;
}