#include <iostream>
#include <string>
#include <set>
#include <unordered_map>
#include <unordered_set>
#include <vector>

using namespace std;

struct Problem {
	int pid, level;

	bool operator<(const Problem& P) const {
		if (level < P.level) return true;
		else if (level > P.level) return false;
		else return pid < P.pid;
	}
};

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	int N;
	cin >> N;

	set<Problem> problems;
	unordered_map<int, unordered_set<int>> mapping;

	for (int i = 0; i < N; i++) {
		Problem prob;
		cin >> prob.pid >> prob.level;
		problems.insert(prob);
		mapping[prob.pid].insert(prob.level);
	}

	int M;
	cin >> M;

	while (M--) {
		string cmd;
		cin >> cmd;

		if (cmd.compare("recommend") == 0) {
			int x;
			cin >> x;

			auto target =
				x == 1
				? --problems.end()
				: problems.begin();

			cout << target->pid << '\n';
		}
		else if (cmd.compare("add") == 0) {
			Problem prob;
			cin >> prob.pid >> prob.level;

			problems.insert(prob);
			mapping[prob.pid].insert(prob.level);
		}
		else {
			int pid;
			cin >> pid;

			for (int level : mapping[pid])
				problems.erase({pid, level});

			mapping.erase(pid);
		}
	}

	return 0;
}