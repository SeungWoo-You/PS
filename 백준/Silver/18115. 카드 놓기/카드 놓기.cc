#include <iostream>

#define MAX_N 1'000'000

using namespace std;

class Deque {
private:
	int arr[MAX_N] = {0};
	int front = -1;
	int rear = -1;
	int dqsize = 0;

public:
	Deque() {
		front = 0;
		rear = 0;
		dqsize = 1;
		arr[front] = 1;
	}

	void tech_1(int x) {
		front = (front - 1 + MAX_N) % MAX_N;
		arr[front] = x;
		dqsize++;
	}

	void tech_2(int x) {
		int temp = arr[front++];
		dqsize--;

		tech_1(x);
		tech_1(temp);
	}

	void tech_3(int x) {
		rear = (rear + 1) % MAX_N;
		arr[rear] = x;
		dqsize++;
	}

	void print() {
		for (int i = 0, j = front; i < dqsize; i++, j = (j + 1) % MAX_N)
			cout << arr[j] << ' ';
	}
};

int orders[MAX_N] = {0};
Deque DQ;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	int N;
	cin >> N;

	for (int i = 0; i < N; i++) cin >> orders[i];

	int card = 2;

	for (int i = N - 2; i >= 0; i--) {
		if (orders[i] == 1) DQ.tech_1(card++);
		else if (orders[i] == 2) DQ.tech_2(card++);
		else DQ.tech_3(card++);
	}

	DQ.print();

	return 0;
}