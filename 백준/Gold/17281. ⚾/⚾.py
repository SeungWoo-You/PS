import sys
from itertools import permutations


if __name__ == '__main__':
    input = sys.stdin.readline
    N = int(input())
    hits = [list(map(int, input().split())) for _ in range(N)]
    score = 0
    for s in permutations(range(1, 9)):
        seq = list(s)
        seq = seq[:3] + [0] + seq[3:]
        i = 0
        temp_score = 0
        for inning in range(N):
            out_count = 0
            bases = [0] * 3
            while out_count < 3:
                hitter = seq[i]
                result = hits[inning][hitter]
                if result == 0:
                    out_count += 1
                else:
                    runner = 0
                    if result == 1:
                        runner += bases[0]
                        bases[0], bases[1] = bases[1], bases[2]
                        bases[2] = 1
                    elif result == 2:
                        runner += bases[0] + bases[1]
                        bases[0] = bases[2]
                        bases[1] = 1
                        bases[2] = 0
                    elif result == 3:
                        runner += bases[0] + bases[1] + bases[2]
                        bases[0] = 1
                        bases[1], bases[2] = 0, 0
                    elif result == 4:
                        runner += bases[0] + bases[1] + bases[2] + 1
                        bases = [0] * 3
                    temp_score += runner
                i = (i + 1) % 9
        score = max(score, temp_score)
    print(score)
