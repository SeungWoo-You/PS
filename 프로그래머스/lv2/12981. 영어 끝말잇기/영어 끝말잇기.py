def solution(n, words):
    checked: set[str] = set()
    last = words[0][0]
    for i, w in enumerate(words):
        if w in checked or last != w[0]:
            quot, rem = divmod(i, n)
            return [rem + 1, quot + 1]
        checked.add(w)
        last = w[-1]
    return [0, 0]