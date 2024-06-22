#include <iostream>
#include <vector>

using namespace std;

void post_order(vector<int>* nodes, int l, int r) {
	if (l >= r) return;

	int root = (*nodes)[l], i = l + 1;
	for (; i < r; i++)
		if ((*nodes)[i] > root) break;
	
	post_order(nodes, l + 1, i);
	post_order(nodes, i, r);
	cout << root << '\n';
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	vector<int> nodes;
	int num;
	while (cin >> num) nodes.push_back(num);

	post_order(&nodes, 0,  (int) nodes.size());

	return 0;
}