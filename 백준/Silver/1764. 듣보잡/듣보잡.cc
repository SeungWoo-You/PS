#include <iostream>
#include <unordered_set>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	int N, M;
	cin >> N >> M;
	
	unordered_set<string> checked;
	while (N--) {
		string name;
		cin >> name;
		checked.insert(name);
	}

	vector<string> answers;
	while (M--) {
		string name;
		cin >> name;

		if (checked.count(name))
			answers.push_back(name);
	}

	sort(answers.begin(), answers.end());
	
	cout << answers.size() << '\n';
	for (string& name : answers)
		cout << name << '\n';

	return 0;
}