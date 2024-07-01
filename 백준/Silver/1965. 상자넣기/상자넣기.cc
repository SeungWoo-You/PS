#include <iostream>
#include <vector>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	int N;
	cin >> N;

	vector<int> boxes(N + 1), lasts;
	for (int i = 1; i <= N; i++) cin >> boxes[i];

	lasts.push_back(boxes[1]);

	for (int i = 2; i <= N; i++) {
		int start = 0, end = (int) lasts.size() - 1;

		while (start <= end) {
			int mid = (start + end) / 2;
			if (lasts[mid] >= boxes[i]) end = mid - 1;
			else start = mid + 1;
		}

		if (start == (int) lasts.size()) lasts.push_back(boxes[i]);
		else lasts[start] = boxes[i];
	}
	
	cout << lasts.size();

	return 0;
}