#include <iostream>

using namespace std; 

int stars[13][3] = {0};
int edge_counts[13] = {0};

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	int targets[4] = {0};
	int target_count = 0;

	for (int i = 0; i < 12; i++) {
		int x, y;
		cin >> x >> y;

		stars[y][edge_counts[y]++] = x;
		stars[x][edge_counts[x]++] = y;

		if (edge_counts[x] == 3)
			targets[target_count++] = x;
		if (edge_counts[y] == 3)
			targets[target_count++] = y;
	}

	for (int tid = 0; tid < target_count; tid++) {
		int t_count = 0;
		int has_leaf = false;
		int star = targets[tid];

		for (int j = 0; j < edge_counts[star]; j++) {
			int near_star = stars[star][j];

			if (edge_counts[near_star] == 3) t_count++;
			if (edge_counts[near_star] == 1) has_leaf = true;
		}

		if (t_count == 1 && has_leaf) {
			cout << star;
			break;
		}
	}

	return 0;
}