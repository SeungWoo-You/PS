#include <iostream>
#include <stack>

using namespace std;

int main() {
	int answer = 0, temp = 1;
	string str;
	stack<char> stk;

	cin >> str;

	for (int i = 0; i < str.length(); i++) {
		if (str[i] == '(') {
			temp *= 2;
			stk.push(str[i]);
		}
		else if (str[i] == ')') {
			if (stk.empty() || stk.top() != '(') {
				answer = 0;
				break;
			}
			else {
				if (str[i - 1] == '(') answer += temp;
				temp /= 2;
				stk.pop();
			}
		}
		else if (str[i] == '[') {
			temp *= 3;
			stk.push(str[i]);
		}
		else if (str[i] == ']') {
			if (stk.empty() || stk.top() != '[') {
				answer = 0;
				break;
			}
			else {
				if (str[i - 1] == '[') answer += temp;
				temp /= 3;
				stk.pop();
			}
		}
	}

	if (!stk.empty()) answer = 0;

	printf("%d", answer);

	return 0;
}