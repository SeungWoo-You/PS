#include <iostream>

#define MAX_N 200'000

using namespace std;

struct Ball {
	int bid;
	int color;
	int size;
};

Ball balls[MAX_N];
Ball temps[MAX_N];
int size_sums[MAX_N + 1] = {0};
int color_sums[MAX_N + 1] = {0};
int results[MAX_N] = {0};

int compare(Ball& A, Ball& B) {
	if (A.size != B.size) {
		return A.size - B.size;
	}
	return A.color - B.color;
}

void merge(int left, int mid, int right) {
	int i = left, j = mid + 1, k = left;

	while (i <= mid && j <= right) {
		if (compare(balls[i], balls[j]) <= 0) temps[k++] = balls[i++];
		else temps[k++] = balls[j++];
	}

	while (i <= mid) temps[k++] = balls[i++];
	while (j <= right) temps[k++] = balls[j++];

	for (int t = left; t <= right; t++)
		balls[t] = temps[t];
}

// 머지 소트 함수
void merge_sort(int left, int right) {
	if (left < right) {
		int mid = (left + right) >> 1;
		merge_sort(left, mid);
		merge_sort(mid + 1, right);
		merge(left, mid, right);
	}
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);

	int N;
	cin >> N;

	for (int i = 0; i < N; i++) {
		cin >> balls[i].color >> balls[i].size;
		balls[i].bid = i;
	}

	merge_sort(0, N - 1);

	int total = 0;
	Ball* prev_ball = nullptr;

	for (int i = 0; i < N; i++) {
		Ball* ball = &balls[i];
		total += ball->size;
		size_sums[ball->size] += ball->size;
		color_sums[ball->color] += ball->size;

		results[ball->bid] = total - color_sums[ball->color] - size_sums[ball->size] + ball->size;
		if (prev_ball != nullptr && prev_ball->color == ball->color && prev_ball->size == ball->size)
			results[ball->bid] = results[prev_ball->bid];

		prev_ball = ball;
	}

	for (int i = 0; i < N; i++)
		cout << results[i] << '\n';

	return 0;
}