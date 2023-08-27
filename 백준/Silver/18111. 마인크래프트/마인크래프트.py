import sys


def main():
    M, N, B = map(int, input().split())
    field = [list(map(int, input().split())) for _ in range(M)]
    res_time = sys.maxsize
    res_h = 0
    for h in range(257):
        dig = 0
        put = 0
        for row in field:
            for ground in row:
                if ground < h:
                    put += h - ground
                elif ground > h:
                    dig += ground - h
        if dig - put + B < 0:
            continue
        exe_time = 2 * dig + put
        if res_time >= exe_time:
            res_time = exe_time
            res_h = h
    print(res_time, res_h, sep=' ')


if __name__ == "__main__":
    input = sys.stdin.readline
    main()
