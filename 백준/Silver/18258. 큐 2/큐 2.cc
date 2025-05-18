#include <iostream>
#define MAX_N 2'000'000

using namespace std;

class Queue {
private:
	int arr[MAX_N] = {0};
	int start = 0;
	int end = -1;
	int qsize = 0;

public:
	void push(int x) {
		arr[++end] = x;
		qsize++;
	}

	int pop() {
		if (empty()) return -1;

		int res = arr[start++];
		qsize--;

		return res;
	}

	bool empty() {
		return qsize == 0;
	}

	int size() {
		return qsize;
	}

	int front() {
		return empty() ? -1 : arr[start];
	}

	int back() {
		return empty() ? -1 : arr[end];
	}
};

Queue Q;

bool compare(char s1[], const char s2[]) {
	for (int i = 0; s1[i] != 0; i++)
		if (s1[i] != s2[i]) return false;

	return true;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	int N, x;
	char cmd[6] = {0};

	cin >> N;

	while (N--) {
		cin >> cmd;

		if (compare(cmd, "push")) {
			cin >> x;
			Q.push(x);
		}
		else if (compare(cmd, "pop"))
			cout << Q.pop() << '\n';
		else if (compare(cmd, "size"))
			cout << Q.size() << '\n';
		else if (compare(cmd, "empty"))
			cout << ((int) Q.empty()) << '\n';
		else if (compare(cmd, "front"))
			cout << Q.front() << '\n';
		else if (compare(cmd, "back"))
			cout << Q.back() << '\n';
	}

	return 0;
}