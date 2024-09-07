#include <iostream>
#include <unordered_set>
#include <deque>
#include <unordered_map>

using namespace std;

bool isin(unordered_map<int, unordered_set<int>>* S, int x, int y) {
	return S->count(x) && (*S)[x].count(y) ? true : false;
}

struct hashFunction {
	size_t operator()(const pair<int, int>& x) const {
		return x.first ^ x.second;
	}

};

class Snake {
private:
	deque<pair<int, int>> pos;
	unordered_map<int, unordered_set<int>> body;
	pair<int, int> direction;
	
public:
	Snake() {
		pos.push_back({1, 1});
		body[1].insert(1);
		direction = {0, 1};
	}

	bool move(int N) {
		pair<int, int> head = pos[0];
		int x = head.first + direction.first,
			y  = head.second + direction.second;

		if (0 < x && x <= N && 0 < y && y <= N
			&& !isin(&body, x, y)) {
			pos.push_front({x, y});
			body[x].insert(y);

			return true;
		}

		return false;
	}

	void eat(unordered_map<int, unordered_set<int>>* apples) {
		pair<int, int> head = pos[0];
		int x = head.first, y = head.second;

		if (isin(apples, x, y))
			apples->at(x).erase(y);
		else {
			int tx = pos.back().first,
				ty = pos.back().second;
			body[tx].erase(ty);
			pos.pop_back();
		}
	}

	void turn(char d) {
		int dx = direction.first,
			dy = direction.second;

		if (d == 'L')
			direction.first = -dy,
			direction.second = dx;
		else if (d == 'D')
			direction.first = dy,
			direction.second = -dx;
	}
};

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	int N, K;
	cin >> N >> K;

	unordered_map<int, unordered_set<int>> apples;
	auto* apples_ptr = &apples;
	Snake snake;
	int sec = 0;

	while (K--) {
		int x, y;
		cin >> x >> y;
		apples[x].insert(y);
	}

	int L;
	cin >> L;

	unordered_map<int, char> turn_infos;
	for (int i = 0; i < L; i++) {
		int x;
		char d;
		cin >> x >> d;
		turn_infos[x] = d;
	}

	while (true) {
		sec += 1;
		if (snake.move(N) == false) break;
		snake.eat(apples_ptr);

		if (turn_infos.count(sec))
			snake.turn(turn_infos[sec]);
	}

	cout << sec;

	return 0;
}