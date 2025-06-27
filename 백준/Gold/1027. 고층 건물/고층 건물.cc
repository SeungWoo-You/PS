#include <iostream>

#define MAX_N 50
#define MAX_STIFF -9'999'999'999;

using namespace std;

int buildings[MAX_N] = {0};
int counts[MAX_N] = {0};

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	int N;
	cin >> N;

	for (int i = 0; i < N; i++) cin >> buildings[i];

	for (int i = 0; i < N; i++) {
		double max_stiff = MAX_STIFF;

		for (int j = i + 1; j < N; j++) {
			double stiff = ((double) (buildings[j] - buildings[i])) / (j - i);

			if (stiff > max_stiff) {
				counts[i]++, counts[j]++;
				max_stiff = stiff;
			}
		}
	}

	int answer = 0;
	
	for (int i = 0; i < N; i++)
		if (answer < counts[i]) answer = counts[i];

	cout << answer;

	return 0;
}