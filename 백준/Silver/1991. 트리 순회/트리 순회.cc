#include <iostream>
#include <unordered_map>

using namespace std;

typedef unordered_map<char, pair<char, char>> TRT;

void preorder(TRT* T, int N, char root) {
	if (root == '.') return;
	
	cout << root;
	preorder(T, N, (*T)[root].first);
	preorder(T, N, (*T)[root].second);
	
	return;
}

void inorder(TRT* T, int N, char root) {
	if (root == '.') return;

	inorder(T, N, (*T)[root].first);
	cout << root;
	inorder(T, N, (*T)[root].second);

	return;
}

void postorder(TRT* T, int N, char root) {
	if (root == '.') return;

	postorder(T, N, (*T)[root].first);
	postorder(T, N, (*T)[root].second);
	cout << root;

	return;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int N;
	cin >> N;

	TRT T;
	for (int i = 0; i < N; i++) {
		char node, L, R;
		cin >> node >> L >> R;
		T[node] = {L, R};
	}

	preorder(&T, N, 'A');
	cout << '\n';
	inorder(&T, N, 'A');
	cout << '\n';
	postorder(&T, N, 'A');

	return 0;
}