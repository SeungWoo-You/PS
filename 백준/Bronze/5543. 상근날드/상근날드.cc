#include <iostream>
#include <algorithm>

using namespace std;

int main() {
	int menus[5], burger, drink;

	for (int i = 0; i < 5; i++) cin >> menus[i];

	burger = *min_element(menus, menus + 3);
	drink = *min_element(menus + 3, menus + 5);
	printf("%d", burger + drink - 50);

	return 0;
}