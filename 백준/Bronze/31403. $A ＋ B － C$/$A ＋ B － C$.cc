#include <iostream>
#include <string>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	string A, B, C;
	cin >> A >> B >> C;

	int s_res = stoi(A + B) - stoi(C);
	int n_res = stoi(A) + stoi(B) - stoi(C);
	cout << n_res << '\n';
	cout << s_res;

	return 0;
}