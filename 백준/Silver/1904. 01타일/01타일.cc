#include <iostream>
#include <cmath>
#include <vector>

#define SIZE 2
#define DIV 15746

using namespace std;

typedef vector<vector<int>> VVIT;
typedef vector<int> VIT;

class FibMat {
public:
	VVIT get_nth_mat(int N) {
		int K = N;
		VVIT temp = _square_matmul(_base, _ident);
		VVIT result(SIZE, VIT(SIZE));
		result = _ident;

		while (K) {
			if (K & 1) result = _square_matmul(result, temp);

			K >>= 1;
			temp = _square_matmul(temp, temp);
		}

		return result;
	}
private:
	VVIT _base{
		{1, 1},
		{1, 0}
	};
	VVIT _ident{
		{1, 0},
		{0, 1}
	};

	VVIT _square_matmul(VVIT A, VVIT B) {
		VVIT result(SIZE, VIT(SIZE));

		for (int i = 0; i < SIZE; i++)
			for (int j = 0; j < SIZE; j++)
				for (int k = 0; k < SIZE; k++)
					result[i][j] = (result[i][j] + (A[i][k] * B[k][j]) % DIV) % DIV;

		return result;
	}
};

int main() {
	int N;
	FibMat mat;

	cin >> N;

	VVIT result = mat.get_nth_mat(N);
	printf("%d", result[0][0]);

	return 0;
}