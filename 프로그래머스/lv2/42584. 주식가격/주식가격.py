def solution(prices):
    answer = [0] * len(prices)
    S: list[tuple[int, int]] = []
    for i, x in enumerate(prices):
        while S and S[-1][1] > x:
            j, _ = S.pop()
            answer[j] = i - j
        S.append((i, x))
    for j, _ in S:
        answer[j] = len(prices) - j - 1
    return answer