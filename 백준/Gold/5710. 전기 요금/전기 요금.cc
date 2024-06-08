#include <iostream>
#include <algorithm>

#define W1 100
#define W2 10000
#define W3 1000000
#define F1 W1 * 2
#define F2 ((W2 - W1) * 3 + F1)
#define F3 ((W3 - W2) * 5 + F2)

using namespace std;

int calc_fee(int elec) {
	int fee = 0;
	
	if (elec <= W1) fee = elec * 2;
	else if (W1 < elec && elec <= W2) fee = F1 + (elec - W1) * 3;
	else if (W2 < elec && elec <= W3) fee = F2 + (elec - W2) * 5;
	else fee = F3 + (elec - W3) * 7;

	return fee;
}

int calc_elec(int fee) {
	int elec = 0;

	if (fee <= F1) elec = fee / 2;
	else if (F1 < fee && fee <= F2) elec = W1 + (fee - F1) / 3;
	else if (F2 < fee && fee <= F3) elec = W2 + (fee - F2) / 5;
	else elec = W3 + (fee - F3) / 7;

	return elec;
}


int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int A, B;
	cin >> A >> B;

	while (A) {
		int elec_sum = calc_elec(A);
		int start = 1, end = elec_sum;
		
		while (start <= end) {
			int my_elec = (start + end) / 2;
			int nei_elec = elec_sum - my_elec;
			int my_fee = calc_fee(my_elec), nei_fee = calc_fee(nei_elec);
			int diff = nei_fee - my_fee;

			if (diff < B) end = my_elec - 1;
			else if (diff > B) start = my_elec + 1;
			else {
				cout << my_fee << '\n';
				break;
			}
		}

		cin >> A >> B;
	}

	return 0;
}