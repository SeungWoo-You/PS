import sys
from dataclasses import dataclass, field


@dataclass
class Ants:
    N: int
    gp: set[str] = field(default_factory=set)


def main():
    N1, N2 = map(int, input().split())
    G1 = ''.join(reversed(input().strip()))
    G2 = input().strip()
    T = int(input())
    a1, a2 = Ants(N1, set(G1)), Ants(N2, set(G2))

    line = G1 + G2
    t = 0
    while t < T:
        temp = ''
        i = 0
        while i < a1.N + a2.N - 1:
            u, v = line[i], line[i + 1]
            if u in a1.gp and v in a2.gp:
                temp = ''.join([temp, v, u])
                i += 2
            else:
                temp += u
                i += 1
        if len(temp) < a1.N + a2.N:
            temp += line[-1]
        line = temp
        t += 1
    print(line)


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
