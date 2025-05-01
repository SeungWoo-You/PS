#include <iostream>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	int W, H, P, Q, T;
	cin >> W >> H >> P >> Q >> T;

	int x_turn = (P + T) / W;
	int y_turn = (Q + T) / H;
	int x_pos = x_turn % 2 ? -(P + T) % W + W : (P + T) % W;
	int y_pos = y_turn % 2 ? -(Q + T) % H + H : (Q + T) % H;
	
	cout << x_pos << ' ' << y_pos;

	return 0;
}