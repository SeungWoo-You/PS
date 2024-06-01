#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

constexpr int SOUND_LEN = 5;

int main() {
	vector<char> ducks;
	string record;
	unordered_map<char, int> sound_order{
		{'q', 0},
		{'u', 1},
		{'a', 2},
		{'c', 3},
		{'k', 4}
	};

	cin >> record;

	for (char rec : record) {
		bool checked = false;

		for (vector<char>::iterator it = ducks.begin(); it != ducks.end(); it++) {
			if ((sound_order[*it] + 1) % SOUND_LEN == sound_order[rec]) {
				*it = rec;
				checked = true;
				break;
			}
		}

		if (!checked) {
			if (rec == 'q') ducks.emplace_back(rec);
			else {
				printf("%d", -1);
				return 0;
			}
		}
	}

	for (char c : ducks) {
		if (c != 'k') {
			printf("%d", -1);
			return 0;
		}
	}

	printf("%zd", ducks.size());

	return 0;
}