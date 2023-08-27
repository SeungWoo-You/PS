def main():
    N = int(input())
    A = list(map(int, input().split()))
    B, C = map(int, input().split())
    print(get_supervisors(A, B, C))


def get_supervisors(A: list[int], B: int, C: int) -> int:
    best_super = 0
    sub_super = 0
    for a in A:
        best_super += 1
        remains = a - B
        if remains <= 0:
            continue
        quot, rem = divmod(remains, C)
        if rem == 0:
            sub_super += quot
        else:
            sub_super += quot + 1
    return best_super + sub_super


if __name__ == '__main__':
    main()
