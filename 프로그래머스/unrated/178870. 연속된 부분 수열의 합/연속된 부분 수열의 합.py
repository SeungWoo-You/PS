def solution(sequence, k):
    possible: list[list[int]] = []
    i, j = 0, -1
    total = 0
    while True:
        if total < k:
            j += 1
            if j >= len(sequence):
                break
            total += sequence[j]
        else:
            total -= sequence[i]
            i += 1
            if i >= len(sequence):
                break
        if total == k:
            possible.append([i, j])
    possible.sort(key=lambda p: p[1] - p[0])
    return possible[0]