#include <iostream>
#include <array>
#include <string>
#include <limits>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	string line;
	cin >> line;

	array<pair<int, int>, 50> level;
	int i = 0, temp_K = 0;

	for (char c : line) {
		if (c == '(') {
			level[i].first -= 1;
			i += 1;
			level[i].second = temp_K;
		}
		else if (c == ')') {
			int length = level[i].first * level[i].second;
			level[i].first = 0;
			i -= 1;
			level[i].first += length;
		}
		else {
			level[i].first += 1;
			temp_K = c - '0';
		}
	}

	cout << level[0].first;
}