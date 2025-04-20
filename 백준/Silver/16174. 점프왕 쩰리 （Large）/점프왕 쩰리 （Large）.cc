#include <iostream>

using namespace std;

#define SIZE 64

struct Data {
	int val = -1;
	int x = -1;
	int y = -1;
};

struct Node {
	Data data;
	Node* prev = nullptr;
	Node* next = nullptr;
};

class Queue {
private:
	int size;
	Node* head;
	Node* tail;

public:
	Queue() {
		this->size = 0;
		this->head = new Node{};
		this->tail = new Node{};
		
		head->next = tail;
		tail->prev = head;
	}

	Node* pop_front() {
		if (size == 0)
			return nullptr;

		Node* node = head->next;
		head->next = node->next;
		node->next->prev = head;
		size--;

		return node;
	}

	void push_back(Data data) {
		Node* node = new Node {data, tail->prev, tail};
		tail->prev->next = node;
		tail->prev = node;
		size++;
	}

	bool empty() {
		return size == 0;
	}

	~Queue() {
		Node* now = head;

		while (now != nullptr) {
			Node* temp = now->next;
			delete now;
			now = temp;
		}
	}
};


int map[SIZE][SIZE];
int N;
Queue Q;
bool visited[SIZE][SIZE] = {false};

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	cin >> N;

	for (int i = 0; i < N; i++)
		for (int j = 0; j < N; j++)
			cin >> map[i][j];

	Q.push_back({map[0][0], 0, 0});
	visited[0][0] = true;

	while (!Q.empty()) {
		Node* node = Q.pop_front();
		Data data = node->data;
		delete node;

		int idx[2] = {data.x, data.x + data.val};
		int jdx[2] = {data.y + data.val, data.y};

		for (int k = 0; k < 2; k++) {
			int i = idx[k], j = jdx[k];

			if (0 <= i && i < N && 0 <= j && j < N && !visited[i][j]) {
				if (map[i][j] == -1) {
					cout << "HaruHaru";

					return 0;
				}

				Q.push_back({map[i][j], i, j});
				visited[i][j] = true;
			}
		}
	}

	cout << "Hing";

	return 0;
}