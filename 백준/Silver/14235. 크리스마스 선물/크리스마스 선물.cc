#include <iostream>
#include <queue>
#include <string>
#include <sstream>
#include <vector>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int N;
	cin >> N;
	cin.ignore();

	priority_queue<int> gifts;

	while (N--) {
		string nums, temp;
		getline(cin, nums);

		stringstream ss(nums);
		vector<string> vec;

		while (getline(ss, temp, ' ')) vec.push_back(temp);

		int a = stoi(vec[0]);

		if (a == 0) {
			if (gifts.empty()) cout << -1 << '\n';
			else {
				cout << gifts.top() << '\n';
				gifts.pop();
			}
		}
		else {
			for (auto it = vec.begin() + 1; it != vec.end(); it++) {
				int g = stoi(*it);
				gifts.emplace(g);
			}
		}
	}
	return 0;
}