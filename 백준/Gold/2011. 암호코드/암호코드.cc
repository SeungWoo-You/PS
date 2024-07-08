#include <iostream>
#include <vector>
#include <string>

#define DIV 1000000;

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	string S;
	cin >> S;

	int N = (int) S.size();
	vector<int> cnts(N + 1, 0);
	cnts[0] = 1;

	if (S[0] != '0') {
		cnts[1] = 1;

		for (int i = 1; i < N; i++) {
			int dig_2 = stoi(S.substr(i - 1, 2));

			if (S[i] != '0') {
				cnts[i + 1] = cnts[i];
				if (10 <= dig_2 && dig_2 <= 26)
					cnts[i + 1] = (cnts[i + 1] + cnts[i - 1]) % DIV;
			}
			else {
				if (10 <= dig_2 && dig_2 <= 26)
					cnts[i + 1] = cnts[i - 1];
				else
					break;
			}
		}
	}

	cout << cnts[N];

	return 0;
}