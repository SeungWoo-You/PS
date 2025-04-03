#include <iostream>

using namespace std;

#define MAX_N 51

int main() {
	int N;
	char seats[MAX_N];

	cin >> N;
	cin >> seats;

	int cup_num = N + 1;

	for (int i = 0; i < N; i++) {
		if (seats[i] == 'L') {
			cup_num--;
			i++;
		}
	}

	printf("%d", cup_num > N ? N : cup_num);

	return 0;
}