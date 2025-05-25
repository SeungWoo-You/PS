#include <iostream>

using namespace std;

int chars[26] = {0};
char name[31];

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	int N;
	cin >> N;

	for (int i = 0; i < N; i++) {
		cin >> name;
		chars[name[0] - 'a']++;
	}

	bool flag = false;

	for (int i = 0; i < 26; i++)
		if (chars[i] >= 5) {
			cout << ((char) (i + 'a'));
			flag = true;
		}

	if (!flag) cout << "PREDAJA";

	return 0;
}