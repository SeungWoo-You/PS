#include <iostream>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	char x[9] = {0};
	int res = 0;
	char operation = ' ';
	
	while (x[0] != '=') {
		cin >> x;
		if ('0' <= x[0] && x[0] <= '9') {
			int num = 0, exp = 1;

			for (int i = 1; x[i] != 0; i++) exp *= 10;
			for (int i = 0; x[i] != 0; i++, exp /= 10) num += (x[i] - '0') * exp;

			if (operation == '+' || operation == ' ') res += num;
			else if (operation == '-') res -= num;
			else if (operation == '*') res *= num;
			else if (operation == '/') res /= num;
		}
		else operation = x[0];
	}

	cout << res;

	return 0;
}