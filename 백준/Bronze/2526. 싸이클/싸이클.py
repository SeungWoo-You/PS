def main():
    N, P = map(int, input().split())
    ls = {N}
    v = N
    cycle_start = False
    count = 0

    start_val = -1
    end_val = -2
    while True:
        v = (v * N) % P
        prev_len = len(ls)
        ls.add(v)
        if prev_len == len(ls):
            if cycle_start == False:
                cycle_start = True
                count = 0
                start_val = v
                end_val = -2
            elif start_val == end_val:
                print(count)
                break
            else:
                end_val = v
                count += 1
        else:
            cycle_start = False


if __name__ == '__main__':
    main()
