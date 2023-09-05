def solution(numbers):
    numbers: list[int]
    answer: list[int] = [-1] * len(numbers)
    stack: list[tuple[int, int]] = []
    for i, n in enumerate(numbers):
        while stack:
            if n > stack[-1][1]:
                j, _ = stack.pop()
                answer[j] = n
            else:
                break
        stack.append((i, n))
    return answer
            