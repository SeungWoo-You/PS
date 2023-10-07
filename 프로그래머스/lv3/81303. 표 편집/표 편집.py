def solution(n, k, cmd):
    answer = ['O'] * n
    table = {i: [i - 1, i + 1] for i in range(n)}
    now = k
    table[0] = [None, 1]
    table[n - 1] = [n - 2, None]
    rmd: list[list[int]] = []
    for T in cmd:
        if T == 'C':
            answer[now] = 'X'
            prev, nxt = table[now]
            rmd.append([prev, now, nxt])
            if nxt == None:
                now = prev
            else:
                now = nxt
            if prev == None:
                table[nxt][0] = None
            elif nxt == None:
                table[prev][1] = None
            else:
                table[prev][1] = nxt
                table[nxt][0] = prev
        elif T == 'Z':
            prev, rec, nxt = rmd.pop()
            answer[rec] = 'O'
            if prev == None:
                table[nxt][0] = rec
            elif nxt == None:
                table[prev][1] = rec
            else:
                table[nxt][0] = rec
                table[prev][1] = rec
        else:
            D, count = T.split()
            count = int(count)
            if D == 'D':
                for _ in range(count):
                    now = table[now][1]
            else:
                for _ in range(count):
                    now = table[now][0]
    return ''.join(answer)