#include <iostream>
#include <vector>
#include <array>
#include <unordered_set>
#include <algorithm>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int N;
	cin >> N;

	vector<int> fruits(N);
	for (int i = 0; i < N; i++) cin >> fruits[i];

	int result = 0;
	int i = 0, fr_count = 0;
	array<int, 10> checked = {0};

	for (int j = 0; j < N; j++) {
		checked[fruits[j]] += 1;

		if (checked[fruits[j]] == 1) fr_count += 1;

		while (fr_count > 2) {
			checked[fruits[i]] -= 1;
			
			if (checked[fruits[i]] == 0) fr_count -= 1;
			i += 1;
		}

		result = max(result, j - i + 1);
	}

	cout << result;

	return 0;
}