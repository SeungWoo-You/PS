#include <iostream>
#include <queue>
#include <array>

#define DIV 10000
#define DIGIT 4

using namespace std;

typedef int func_t(int);
typedef func_t* pfunc_t;

int command_D(int n) {
	return (2 * n) % DIV;
}

int command_S(int n) {
	return (n - 1 + DIV) % DIV;
}

int command_L(int n) {
	return (n % 1000) * 10 + n / 1000;
}

int command_R(int n) {
	return (n % 10) * 1000 + n / 10;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int T;
	cin >> T;

	array<pair<char, pfunc_t>, 4> commands {
		{
			{'D', command_D}, {'S',command_S}, {'L',command_L}, {'R',command_R}
		}
	};

	while (T--) {
		int A, B;
		cin >> A >> B;

		queue<pair<int, string>> Q;
		array<bool, DIV> checked {false};

		Q.push({A, ""});

		while (!Q.empty()) {
			auto [n, seq] = Q.front();
			Q.pop();

			if (n == B) {
				cout << seq << '\n';
				break;
			}

			for (auto p : commands) {
				int temp_n = p.second(n);
				string temp_seq = seq + p.first;

				if (checked[temp_n] == false) {
					checked[temp_n] = true;
					Q.push({temp_n, temp_seq});
				}
			}
		}
	}

	return 0;
}