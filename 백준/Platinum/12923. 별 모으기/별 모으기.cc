#include <iostream>
#include <algorithm>
#include <deque>

#define MAX_N 1000
#define MAX_VAL (~0U >> 2)

using namespace std;

deque<pair<int, int>> stages;

bool compare(pair<int, int>& A, pair<int, int>& B) {
	return A.second < B.second;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	int N;
	cin >> N;

	for (int i = 0; i < N; i++) {
		int a, b;
		cin >> a >> b;
		stages.push_back({a, b});
	}

	sort(stages.begin(), stages.end(), compare);

	int sid = 0;
	int star = 0, count = 0;
	
	while (!stages.empty()) {
		if (stages[0].second <= star) {
			star++;
			count++;
			if (stages[0].first != MAX_VAL) star++;
			stages.pop_front();
		}
		else {
			int prev_star = star;

			for (int i = stages.size() - 1; i >= 0; i--) {
				if (stages[i].first <= star) {
					stages[i].first = MAX_VAL;
					star++;
					count++;
					break;
				}
			}
			if (star == prev_star) {
				cout << "Too Bad";
				return 0;
			}
		}
	}

	cout << count;

	return 0;
}