#include <iostream>

#define MAX_N 1000
#define MAX_LEN 9
#define DIGIT 36
#define HASH_SIZE 3001

using namespace std;

long long car_id_to_num(char car_id[MAX_LEN]) {
	long long num = 0;

	for (int i = 0, exp = 1; car_id[i] != 0; i++, exp *= DIGIT) {
		if ('0' <= car_id[i] && car_id[i] <= '9')
			num += ((long long) car_id[i] - '0') * exp;
		else
			num += ((long long) car_id[i] - 'A' + 10) * exp;
	}

	return num;
}

class CarMap {
private:
	long long hash_keys[HASH_SIZE] = {0};
	int hash_vals[HASH_SIZE] = {0};

	int hash(long long cnum) {
		return (cnum % HASH_SIZE + HASH_SIZE) % HASH_SIZE;
	}

public:
	CarMap() {
		for (int i = 0; i < HASH_SIZE; i++) hash_keys[i] = -1;
	}

	void insert(long long cnum, int order) {
		int h = hash(cnum);

		while (hash_keys[h] != -1)
			h = (h + 1) % HASH_SIZE;

		hash_keys[h] = cnum;
		hash_vals[h] = order;
	}

	int find(long long cnum) {
		int h = hash(cnum);

		while (hash_keys[h] != -1) {
			if (hash_keys[h] == cnum) return hash_vals[h];
			h = (h + 1) % HASH_SIZE;
		}

		return -1;
	}
};

long long out_nums[MAX_N] = {0};
CarMap in_map = CarMap();

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	int N;
	cin >> N;

	char car_id[MAX_LEN] = {0};
	int count = 0;

	for (int i = 0; i < N; i++) {
		cin >> car_id;
		long long car_num = car_id_to_num(car_id);
		in_map.insert(car_num, i);
	}

	for (int i = 0; i < N; i++) {
		cin >> car_id;
		out_nums[i] = car_id_to_num(car_id);
	}

	for (int i = 0; i < N; i++) {
		int now_order = in_map.find(out_nums[i]);

		for (int j = i + 1; j < N; j++)
			if (now_order > in_map.find(out_nums[j])) {
				count++;
				break;
			}
	}

	cout << count;

	return 0;
}