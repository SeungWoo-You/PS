#include <iostream>

#define MAX_N 15

using namespace std;

int nums[MAX_N] = {0};

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	while (true) {
		int x, size = 0, count = 0;
		cin >> x;

		if (x == -1) break;

		while (x != 0) {
			nums[size++] = x;
			cin >> x;
		}

		for (int i = 0; i < size; i++)
			for (int j = i + 1; j < size; j++)
				if ((nums[i] << 1) == nums[j]
					|| (nums[j] << 1) == nums[i]) count++;

		cout << count << '\n';
	}


	return 0;
}