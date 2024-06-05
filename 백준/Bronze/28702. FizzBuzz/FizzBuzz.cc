#include <iostream>
#include <array>
#include <string>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	array<string, 3> arr;
	for (int i = 0; i < 3; i++) cin >> arr[i];

	int idx = 0, num = 0;
	
	for (; idx < 3; idx++) {
		num = atoi(arr[idx].c_str());
		
		if (num != 0) break;
	}
	
	num += 3 - idx;
	int rem_3 = num % 3, rem_5 = num % 5;
	
	if (rem_3 == 0 && rem_5 == 0) cout << "FizzBuzz";
	else if (rem_3 == 0) cout << "Fizz";
	else if (rem_5 == 0) cout << "Buzz";
	else cout << num;

	return 0;
}