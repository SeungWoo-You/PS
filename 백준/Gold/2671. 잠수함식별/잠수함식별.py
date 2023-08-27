def main():
    sound = list(map(int, list(input())))
    N = len(sound)
    idx = 0
    state = True
    while state == True and idx < N:
        if sound[idx] == 0:
            state, idx = is_01(sound, idx, N)
        elif sound[idx] == 1:
            state, idx = is_1001(sound, idx, N)
        idx += 1
    if state == False or idx < N:
        print("NOISE")
    else:
        print("SUBMARINE")


def is_01(sound: list[int], idx: int, N: int) -> tuple[bool, int]:
    if idx + 1 == N or sound[idx + 1] != 1:
        state = False
    else:
        state = True
    return (state, idx + 1)


def is_1001(sound: list[int], idx: int, N: int) -> tuple[bool, int]:
    if idx + 3 >= N:
        return (False, idx + 3)
    check_100 = sound[idx: idx + 3]
    if check_100 != [1, 0, 0]:
        return (False, idx + 2)
    idx = skip_repeat(sound, idx, N, 0)
    if idx + 1 == N:
        return (False, idx)
    temp = idx
    idx = skip_repeat(sound, idx, N, 1)
    if idx - temp == 1:
        pass
    elif idx + 2 < N and sound[idx + 2] == 0:
        idx = idx - 1
    return (True, idx)


def skip_repeat(sound: list[int], idx: int, N: int, binary: int) -> int:
    for i in range(idx + 1, N):
        if i + 1 == N or sound[i + 1] != binary:
            break
    return i


if __name__ == '__main__':
    main()
