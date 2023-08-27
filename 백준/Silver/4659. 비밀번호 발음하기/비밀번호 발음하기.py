import sys


def main():
    vowel = {'a', 'e', 'i', 'o', 'u'}
    pw = input().strip()

    while pw != 'end':
        seq = 0
        prev = ''
        contained = False
        keep = True
        for c in pw:
            if keep == False:
                break
            if c in vowel:
                contained = True
            if {c, prev} & vowel == {c, prev} or {c, prev} & vowel == set():
                seq += 1
            else:
                seq = 1
            if seq == 3:
                keep = False
            if c not in {'e', 'o'} and c == prev:
                keep = False
            prev = c
        if keep == True and contained == True:
            print(f'<{pw}> is acceptable.')
        else:
            print(f'<{pw}> is not acceptable.')
        pw = input().strip()


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
