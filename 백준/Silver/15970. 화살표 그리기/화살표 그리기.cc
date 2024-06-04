#include <iostream>
#include <unordered_map>
#include <vector>
#include <algorithm>
#include <cstdlib>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int N;
	cin >> N;

	unordered_map<int, vector<int>> coords;

	for (int i = 0; i < N; i++) {
		int x, color;
		cin >> x >> color;

		coords[color].push_back(x);
	}

	int total = 0;

	for (auto& [_, vec] : coords) {
		sort(vec.begin(), vec.end());
		size_t size = vec.size();

		for (int i = 0; i < size; i++) {
			if (i == 0) total += abs(vec[i] - vec[i + 1]);
			else if (i == size - 1) total += abs(vec[i - 1] - vec[i]);
			else total += min(abs(vec[i - 1] - vec[i]), abs(vec[i] - vec[i + 1]));
		}
	}

	cout << total;

	return 0;
}