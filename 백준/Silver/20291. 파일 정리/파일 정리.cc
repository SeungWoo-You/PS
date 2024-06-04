#include <iostream>
#include <map>
#include <sstream>
#include <vector>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int N;
	cin >> N;

	map<string, int> files;

	for (int i = 0; i < N; i++) {
		string fname, temp;
		cin >> fname;
		
		vector<string> vec;
		stringstream ss(fname);

		while (getline(ss, temp, '.')) vec.emplace_back(temp);

		files[vec[1]] += 1;
	}

	for (const auto& [ext, count] : files) cout << ext << ' ' << count << '\n';

	return 0;
}